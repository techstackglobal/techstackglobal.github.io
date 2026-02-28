import os
import argparse
import json
import subprocess
from typing import Optional, List, Dict
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class ClaudeClient:
    """
    A unified client for interacting with Anthropic's Claude 4.6 Sonnet model.
    Uses 'curl.exe' as a backend to bypass certain OS/Firewall restrictions that 
    block Python networking libraries from sending API keys.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Anthropic API Key not found. Please set 'ANTHROPIC_API_KEY' "
                "in your environment or .env file."
            )
        self.base_url = "https://api.anthropic.com/v1/messages"
        self.model = "claude-sonnet-4-6"

    def _call_curl(self, data: dict, stream: bool = False) -> str:
        """
        Calls the Anthropic API using system curl.exe.
        """
        # Create a temporary JSON file for the data to avoid command line length issues
        temp_file = "claude_req.json"
        with open(temp_file, "w") as f:
            json.dump(data, f)

        cmd = [
            "curl.exe", "-s", "-X", "POST", self.base_url,
            "-H", f"x-api-key: {self.api_key}",
            "-H", "anthropic-version: 2023-06-01",
            "-H", "content-type: application/json",
            "--data-binary", f"@{temp_file}"
        ]

        if stream:
            # For streaming, we need to parse the SSE output manually
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            full_text = []
            for line in process.stdout:
                if line.startswith("data: "):
                    try:
                        event_data = json.loads(line[6:])
                        if event_data["type"] == "content_block_delta":
                            text = event_data["delta"]["text"]
                            print(text, end="", flush=True)
                            full_text.append(text)
                    except:
                        pass
            print()
            os.remove(temp_file)
            return "".join(full_text)
        else:
            result = subprocess.run(cmd, capture_output=True, text=True)
            os.remove(temp_file)
            
            if result.returncode != 0:
                return f"Error executing curl: {result.stderr}"
            
            try:
                response_json = json.loads(result.stdout)
                if "error" in response_json:
                    error_msg = response_json["error"]["message"]
                    # Check for credit-related errors
                    if "credit" in error_msg.lower() or "balance" in error_msg.lower():
                        return f"CRITICAL ERROR: Credit Exhaustion. {error_msg}\nPlease top up your Anthropic account."
                    return f"API Error: {error_msg}"
                return response_json["content"][0]["text"]
            except Exception as e:
                return f"Error parsing response: {e}\nRaw Output: {result.stdout}"

    def ask(self, prompt: str, system_prompt: Optional[str] = None, max_tokens: int = 4096) -> str:
        data = {
            "model": self.model,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}]
        }
        if system_prompt:
            data["system"] = system_prompt
        return self._call_curl(data)

    def stream_ask(self, prompt: str, system_prompt: Optional[str] = None):
        data = {
            "model": self.model,
            "max_tokens": 4096,
            "messages": [{"role": "user", "content": prompt}],
            "stream": True
        }
        if system_prompt:
            data["system"] = system_prompt
        return self._call_curl(data, stream=True)

def main():
    parser = argparse.ArgumentParser(description="Claude 4.6 Sonnet API Integration (Bypass Mode)")
    parser.add_argument("--test", action="store_true", help="Run a simple connectivity test")
    parser.add_argument("--prompt", type=str, help="Prompt to send to Claude")
    parser.add_argument("--stream", action="store_true", help="Stream the response")
    
    args = parser.parse_args()
    
    try:
        client = ClaudeClient()
        
        if args.test:
            print(f"Testing connectivity to model: {client.model}...")
            response = client.ask("Confirm you are Sonnet 4.6 and our connection via curl is working.")
            print(f"\nResponse: {response}")
        elif args.prompt:
            if args.stream:
                client.stream_ask(args.prompt)
            else:
                response = client.ask(args.prompt)
                print(response)
        else:
            parser.print_help()
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

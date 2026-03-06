import pathlib
import re

file_path = pathlib.Path("posts/best-ultrawide-monitor-for-programming-2026.html")
content = file_path.read_text(encoding="utf-8")

# Replace ASINs
content = content.replace("B0BQSLL3J2", "B0BP94JZCZ")
content = content.replace("B0DKX5T4XT", "B0BLF2RWNV")

# Replace comparison table
table_replacement = """<div class="table-responsive">
<table>
<thead>
<tr>
<th>Monitor</th>
<th>Panel Type</th>
<th>Resolution</th>
<th>Best Use</th>
</tr>
</thead>

<tbody>

<tr>
<td>Alienware AW3423DWF</td>
<td>QD-OLED</td>
<td>3440×1440</td>
<td>Programming + creative work</td>
</tr>

<tr>
<td>Samsung Odyssey G8</td>
<td>OLED</td>
<td>3440×1440</td>
<td>Programming + entertainment</td>
</tr>

<tr>
<td>LG 34GP83A-B</td>
<td>IPS</td>
<td>3440×1440</td>
<td>Pure coding and text clarity</td>
</tr>

</tbody>
</table>
</div>"""

pattern = re.compile(r'<div\s+class="table-responsive">.*?</div>', re.DOTALL)
if pattern.search(content):
    content = pattern.sub(table_replacement, content, count=1)
    print("Table replaced.")
else:
    print("Table not found.")

file_path.write_text(content, encoding="utf-8")
print("ASINs and table replaced successfully.")

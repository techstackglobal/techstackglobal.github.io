import shutil
src1 = r"C:\Users\PMLS\.gemini\antigravity\brain\8acb5e45-297b-4c05-ae50-1d7cdeac50b0\media__1772154222166.jpg"
src2 = r"C:\Users\PMLS\.gemini\antigravity\brain\8acb5e45-297b-4c05-ae50-1d7cdeac50b0\media__1772154257524.jpg"
dst1a = r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\posts\lg-27us500w-primary.jpg"
dst1b = r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\assets\images\products\lg-27us500w-primary.jpg"
dst2a = r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\posts\lg-27us500w-secondary.jpg"
dst2b = r"c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\assets\images\products\lg-27us500w-secondary.jpg"
shutil.copy2(src1, dst1a)
shutil.copy2(src1, dst1b)
shutil.copy2(src2, dst2a)
shutil.copy2(src2, dst2b)
print("All 4 files copied successfully.")

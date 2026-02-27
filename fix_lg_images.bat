@echo off
SET BRAIN=C:\Users\PMLS\.gemini\antigravity\brain\8acb5e45-297b-4c05-ae50-1d7cdeac50b0
SET POSTS=c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\posts
SET ASSETS=c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog\assets\images\products

echo Copying LG primary image...
copy /Y "%BRAIN%\media__1772154222166.jpg" "%POSTS%\lg-27us500w-primary.jpg"
copy /Y "%BRAIN%\media__1772154222166.jpg" "%ASSETS%\lg-27us500w-primary.jpg"

echo Copying LG secondary image...
copy /Y "%BRAIN%\media__1772154257524.jpg" "%POSTS%\lg-27us500w-secondary.jpg"
copy /Y "%BRAIN%\media__1772154257524.jpg" "%ASSETS%\lg-27us500w-secondary.jpg"

echo.
echo Verifying files:
if exist "%POSTS%\lg-27us500w-primary.jpg" (echo PRIMARY in posts: OK) else (echo PRIMARY in posts: MISSING)
if exist "%POSTS%\lg-27us500w-secondary.jpg" (echo SECONDARY in posts: OK) else (echo SECONDARY in posts: MISSING)
if exist "%ASSETS%\lg-27us500w-primary.jpg" (echo PRIMARY in assets: OK) else (echo PRIMARY in assets: MISSING)

echo.
echo DONE.
pause

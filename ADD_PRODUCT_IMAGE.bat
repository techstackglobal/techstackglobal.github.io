@echo off
:: =============================================
:: TechStack Global - Add Product Image Tool
:: =============================================
:: HOW TO USE:
::   DRAG AND DROP an image file onto this .bat file
::   OR run: add_product_image.bat "C:\path\to\image.jpg" "product-name" primary
::
:: EXAMPLES:
::   add_product_image.bat "C:\Users\Me\Desktop\monitor.jpg" "samsung-32-4k" primary
::   add_product_image.bat "C:\Users\Me\Desktop\ports.jpg" "samsung-32-4k" secondary

SETLOCAL

SET BLOG_DIR=c:\Users\PMLS\Desktop\Youtube Shorts\b2b_blog

:: ---- If dragged onto bat file, use first arg as image ----
IF "%~1"=="" (
    echo.
    echo  TechStack Global - Add Product Image
    echo  =====================================
    echo  HOW TO USE:
    echo.
    echo  1. DRAG AND DROP your image onto this file, OR
    echo  2. Run: add_product_image.bat "image.jpg" "product-name" primary/secondary
    echo.
    echo  EXAMPLES:
    echo    add_product_image.bat "C:\photo.jpg" "samsung-32-4k" primary
    echo    add_product_image.bat "C:\photo.jpg" "samsung-32-4k" secondary
    echo.
    pause
    EXIT /B
)

SET SOURCE_IMAGE=%~1

:: ---- If only 1 arg (drag+drop), prompt for name and type ----
IF "%~2"=="" (
    echo.
    echo Image: %SOURCE_IMAGE%
    echo.
    SET /P PRODUCT_NAME=Enter product name (e.g. samsung-32-4k): 
    SET /P IMAGE_TYPE=Primary or secondary? (primary/secondary): 
) ELSE (
    SET PRODUCT_NAME=%~2
    SET IMAGE_TYPE=%~3
    IF "%IMAGE_TYPE%"=="" SET IMAGE_TYPE=primary
)

SET DEST_NAME=%PRODUCT_NAME%-%IMAGE_TYPE%.jpg
SET POSTS_DEST=%BLOG_DIR%\posts\%DEST_NAME%
SET ASSETS_DEST=%BLOG_DIR%\assets\images\products\%DEST_NAME%

echo.
echo Copying "%SOURCE_IMAGE%"
echo   -> posts\%DEST_NAME%
echo   -> assets\images\products\%DEST_NAME%
echo.

copy /Y "%SOURCE_IMAGE%" "%POSTS_DEST%"
copy /Y "%SOURCE_IMAGE%" "%ASSETS_DEST%"

IF EXIST "%POSTS_DEST%" (
    echo SUCCESS! Image saved.
    echo.
    echo Now use this path in your HTML:
    echo.
    echo   In posts/your-review.html:    src="%DEST_NAME%"
    echo   In blog.html or other pages:  src="assets/images/products/%DEST_NAME%"
    echo.
) ELSE (
    echo ERROR: Copy failed. Check the source path.
)

pause

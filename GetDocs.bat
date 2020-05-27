@ECHO OFF

REM Pygeostat Document
CALL conda activate Geostat

ECHO Building Pygeostat documentation...

CALL ..\pygeostat_public\doc\make.bat clean

CALL ..\pygeostat_public\doc\make.bat html

ECHO Copying Pygeostat documentation...

xcopy /s/e/y ..\pygeostat_public\doc\build\html .\static\Pygeostat

git checkout master

git add .

git commit -am "Updated pygeostat documentation"

git push


REM Data Analysis Documents

ECHO Building Data analysis documentation...

CALL ..\Lessons\DataAnalysis\make.bat clean

CALL ..\Lessons\DataAnalysis\make.bat html

ECHO Copying Pygeostat documentation...

xcopy /s/e/y ..\Lessons\DataAnalysis\build\html .\static\DataAnalysis

git checkout master

git add .

git commit -am "Updated data analysis documentation"

git push

ECHO Done
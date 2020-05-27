@ECHO OFF

REM CALL conda activate Geostat

REM ECHO Building Pygeostat documentation...

REM CALL ..\pygeostat_public\doc\make.bat clean

REM CALL ..\pygeostat_public\doc\make.bat html

ECHO Copying Pygeostat documentation...

xcopy /s/e/y ..\pygeostat_public\doc\build\html .\static\Pygeostat

git checkout master

git add .

git commit -am "Updated pygeostat documentation"

git push

ECHO Done
@ECHO OFF

CALL conda activate Geostat

ECHO Building Pygeostat documentation...

CALL ..\pygeostat_public\doc\make.bat clean

CALL ..\pygeostat_public\doc\make.bat html

ECHO Copying Pygeostat documentation...

xcopy /s/e/y ..\pygeostat_public\doc\build\html .\static\Pygeostat

ECHO Done
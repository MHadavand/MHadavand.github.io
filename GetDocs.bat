@ECHO OFF

ECHO Copying Pygeostat documentation...

xcopy /s/e ..\pygeostat_public\doc\build\html .\static\Pygeostat -A

ECHO Done
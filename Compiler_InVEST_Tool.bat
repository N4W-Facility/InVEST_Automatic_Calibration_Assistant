@echo off
setlocal EnableDelayedExpansion

echo ========================================
echo  InVEST Calibrator - Compilacion Automatica
echo  Generado por DependencyAnalyzer
echo ========================================
echo.

REM Verificar si conda está disponible
where conda >nul 2>&1
if errorlevel 1 (
    echo Intentando activar conda desde ruta base...
    if exist "C:\Users\jonathan.nogales\AppData\Local\anaconda3\Scripts\conda.exe" (
        call "C:\Users\jonathan.nogales\AppData\Local\anaconda3\Scripts\activate.bat" "C:\Users\jonathan.nogales\AppData\Local\anaconda3\envs\InVEST_Tool"
    ) else (
        echo ERROR: No se puede encontrar conda
        echo Asegurate de que conda este en el PATH o ejecuta desde Anaconda Prompt
        pause
        exit /b 1
    )
) else (
    echo Activando entorno InVEST...
    call conda activate InVEST_Tool
)

REM Verificar que pyinstaller esté disponible
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo ERROR: PyInstaller no está instalado en el entorno
    echo Instalando PyInstaller...
    pip install pyinstaller
)

REM Limpiar compilaciones anteriores
echo Limpiando archivos anteriores...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
if exist "*.spec" del "*.spec"

echo.
echo ========================================
echo Iniciando compilacion con PyInstaller...
echo ========================================
echo.

REM Crear comando pyinstaller línea por línea para evitar problemas
set PYINSTALLER_CMD=pyinstaller
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --name InVEST_Calibration_Assistant
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --clean
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --onefile
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --windowed
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --collect-all rasterio
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --collect-all geopandas
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --collect-all shapely
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --collect-all pyproj
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --collect-all fiona
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --collect-all natcap
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --collect-all pyogrio
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --collect-all spotpy
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --collect-submodules pandas
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --collect-all osgeo
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --collect-all simpledbf

REM Módulos core de rasterio
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio._io"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.sample"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.crs"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.transform"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.warp"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.mask"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.features"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.windows"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.coords"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.plot"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.merge"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.vrt"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.rio"

REM Submódulos adicionales
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.control"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.fill"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.shutil"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.path"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.session"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.env"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.errors"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.enums"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.drivers"

REM Submódulos de herramientas rio
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.rio.main"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.rio.info"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.rio.insp"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.rio.sample"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.rio.shapes"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.rio.rasterize"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.rio.mask"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.rio.merge"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.rio.overview"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.rio.translate"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "rasterio.rio.warp"

set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "pyogrio._geometry"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "pyogrio._io"
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import "pyogrio._env"

set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=spotpy.database.csv
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=spotpy.database.ram
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=spotpy.algorithms.lhs
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=spotpy.algorithms.dds
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=spotpy.algorithms.sceua

set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=osgeo.gdal
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=osgeo.ogr
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=osgeo.osr
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=osgeo.gdal_array

set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=numpy
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=pandas
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=tkinter
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=win32com.client

set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=natcap.invest.seasonal_water_yield.seasonal_water_yield
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=natcap.invest.sdr.sdr
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=natcap.invest.ndr.ndr
set PYINSTALLER_CMD=!PYINSTALLER_CMD! --hidden-import=natcap.invest.annual_water_yield

REM Agregar datos críticos
if exist "C:\Users\jonathan.nogales\AppData\Local\anaconda3\envs\InVEST_Tool\Library\share" (
    set PYINSTALLER_CMD=!PYINSTALLER_CMD! --add-data "C:\Users\jonathan.nogales\AppData\Local\anaconda3\envs\InVEST_Tool\Library\share;Library\share"
)

REM Agregar DLLs críticos (expandidos uno a uno para evitar problemas con comodines)
for %%f in ("C:\Users\jonathan.nogales\AppData\Local\anaconda3\envs\InVEST_Tool\Library\bin\*.dll") do (
    call set PYINSTALLER_CMD=%%PYINSTALLER_CMD%% --add-binary "%%f;."
)

REM Agregar DLLs GDAL
for %%f in ("%CONDA_PREFIX%\Library\bin\gdal*.dll") do (
    call set PYINSTALLER_CMD=%%PYINSTALLER_CMD%% --add-binary "%%f;."
)

REM Agregar DLLs PROJ
for %%f in ("%CONDA_PREFIX%\Library\bin\proj_*.dll") do (
    call set PYINSTALLER_CMD=%%PYINSTALLER_CMD%% --add-binary "%%f;."
)

REM Agregar DLLs GEOS
for %%f in ("%CONDA_PREFIX%\Library\bin\geos*.dll") do (
    call set PYINSTALLER_CMD=%%PYINSTALLER_CMD%% --add-binary "%%f;."
)

REM Agregar el script principal
set PYINSTALLER_CMD=!PYINSTALLER_CMD! "InVEST_AutoCalTools.py"

echo Ejecutando: !PYINSTALLER_CMD!
echo.

REM Ejecutar PyInstaller
!PYINSTALLER_CMD!

echo.
if exist "dist\InVEST_Calibration_Assistant.exe" (
    echo ========================================
    echo  COMPILACION EXITOSA!
    echo  Ejecutable creado en: dist\InVEST_Calibration_Assistant.exe
    echo  Tamaño: 
    dir "dist\InVEST_Calibration_Assistant.exe" | find "InVEST_Calibration_Assistant.exe"
    echo ========================================
    echo.
    echo ¿Deseas ejecutar el programa compilado? (s/n)
    set /p ejecutar=
    if /i "!ejecutar!"=="s" (
        start "" "dist\InVEST_Calibration_Assistant.exe"
    )
) else (
    echo ========================================
    echo  ERROR EN LA COMPILACION
    echo  Revisa los mensajes anteriores
    echo ========================================
    echo.
    echo Posibles soluciones:
    echo 1. Ejecutar desde Anaconda Prompt
    echo 2. Verificar que todas las dependencias estén instaladas
    echo 3. Revisar el archivo dependency_report.txt
    echo 4. Ejecutar: pip install pyinstaller
)

echo.
echo Presiona cualquier tecla para continuar...
pause >nul

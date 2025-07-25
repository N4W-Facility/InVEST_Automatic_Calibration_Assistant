# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_all

datas = [('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\share', 'Library\\share')]
binaries = [('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-console-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-console-l1-2-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-datetime-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-debug-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-errorhandling-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-fibers-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-file-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-file-l1-2-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-file-l2-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-handle-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-heap-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-interlocked-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-libraryloader-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-localization-l1-2-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-memory-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-namedpipe-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-processenvironment-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-processthreads-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-processthreads-l1-1-1.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-profile-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-rtlsupport-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-string-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-synch-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-synch-l1-2-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-sysinfo-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-timezone-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-core-util-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-conio-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-convert-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-environment-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-filesystem-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-heap-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-locale-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-math-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-multibyte-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-private-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-process-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-runtime-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-stdio-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-string-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-time-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\api-ms-win-crt-utility-l1-1-0.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\archive.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\blosc.dll', '.'), ('C:\\Users\\jonathan.nogales\\AppData\\Local\\anaconda3\\envs\\InVEST_Tool\\Library\\bin\\brotlicommon.dll', '.')]
hiddenimports = ['rasterio._io', 'rasterio.sample', 'rasterio.crs', 'rasterio.transform', 'rasterio.warp', 'rasterio.mask', 'rasterio.features', 'rasterio.windows', 'rasterio.coords', 'rasterio.plot', 'rasterio.merge', 'rasterio.vrt', 'rasterio.rio', 'rasterio.control', 'rasterio.fill', 'rasterio.shutil', 'rasterio.path', 'rasterio.session', 'rasterio.env', 'rasterio.errors', 'rasterio.enums', 'rasterio.drivers', 'rasterio.rio.main', 'rasterio.rio.info', 'rasterio.rio.insp', 'rasterio.rio.sample', 'rasterio.rio.shapes', 'rasterio.rio.rasterize', 'rasterio.rio.mask', 'rasterio.rio.merge', 'rasterio.rio.overview', 'rasterio.rio.translate', 'rasterio.rio.warp', 'pyogrio._geometry', 'pyogrio._io', 'pyogrio._env', 'spotpy.database.csv', 'spotpy.database.ram', 'spotpy.algorithms.lhs', 'spotpy.algorithms.dds', 'spotpy.algorithms.sceua', 'osgeo.gdal', 'osgeo.ogr', 'osgeo.osr', 'osgeo.gdal_array', 'numpy', 'pandas', 'tkinter', 'win32com.client', 'natcap.invest.seasonal_water_yield.seasonal_water_yield', 'natcap.invest.sdr.sdr', 'natcap.invest.ndr.ndr', 'natcap.invest.annual_water_yield']
hiddenimports += collect_submodules('pandas')
tmp_ret = collect_all('rasterio')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('geopandas')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('shapely')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('pyproj')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('fiona')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('natcap')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('pyogrio')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('spotpy')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('osgeo')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('simpledbf')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['InVEST_AutoCalTools.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='InVEST_Calibration_Assistant',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

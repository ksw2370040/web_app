# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Collect all submodules and data files for Django
hiddenimports = collect_submodules('django') + [
    'widget_tweaks',
    'stdimage',
    'django.utils.autoreload',
]

datas = collect_data_files('django') + [
    ('C:/web_app/kashi_wa/media', 'media'),
    ('C:/web_app/kashi_wa/kashi_wa', 'kashi_wa'),
    ('C:/web_app/kashi_wa/gameapp', 'gameapp'),
    ('C:/web_app/kashi_wa/accounts', 'accounts'),
]

a = Analysis(
    ['manage.py'],
    pathex=['C:/web_app/kashi_wa'],
    binaries=[],
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
    name='manage',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

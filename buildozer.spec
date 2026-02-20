[app]

# (str) Title of your application
title = Sofia Mobile

# (str) Package name
package.name = sofiamobile

# (str) Package domain (needed for android/ios packaging)
package.domain = org.julio.sofia

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let extensions blank to include all)
source.include_exts = py,png,jpg,kv,atlas,json,appicon,webicon,manifest

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3, kivy==2.3.0, kivymd, pillow, android, cython==0.29.33

# (str) python-for-android branch to use, defaults to master
p4a.branch = master

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, VIBRATE, QUERY_ALL_PACKAGES, WRITE_SETTINGS, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, BLUETOOTH, BLUETOOTH_ADMIN, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, KILL_BACKGROUND_PROCESSES

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support. (API 21 = Android 5.0)
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (list) The Android archs to build for (Focado no Tablet)
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backups feature (Android API >=23)
android.allow_backup = True

# (list) Exclude unsupported extensions
android.exclude_exts = _lzma,_uuid,grp

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

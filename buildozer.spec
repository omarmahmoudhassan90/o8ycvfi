[app]
# (str) Title of your application
title = سباق الرواد
# (str) Package name
package.name = racegame
# (str) Package domain (reverse domain)
package.domain = org.alrowad
# (list) Source files to include (comma separated)
source.include_exts = py,kv,png,jpg,atlas
# (list) Application requirements
requirements = python3,kivy==2.1.0,requests
# (str) Supported orientation (landscape, portrait or all)
orientation = portrait
# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1
# (int) Android API to use
android.api = 31
# (int) Minimum Android API your APK will support
android.minapi = 21
# (str) Android NDK version to use
android.ndk = 23b
# (str) Android SDK version (build tools)
#android.sdk = 24
# (str) Presplash / icon placeholders
#icon.filename = %(source.dir)s/icon.png

# (str) Application entry point, default is main.py
#entrypoint = main.py

# (bool) If True, the app will be packaged with a shared library
# use 'p4a.branch' or configure other p4a options if necessary

# (str) Log level
log_level = 2
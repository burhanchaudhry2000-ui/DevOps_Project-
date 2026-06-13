# eyedoc_updated

A new Flutter project.

## Getting Started

This project is a starting point for a Flutter application.

## Build prerequisites

- Install **Flutter SDK** (a full install, not just `bin/`)
- Install **Android Studio** (or Android SDK + platform tools)

## Configure Flutter SDK path (per machine)

This repo does **not** hardcode a Flutter path (every machine is different). The Android build will use one of:

- `FLUTTER_ROOT` environment variable (recommended), or
- `android/local.properties` with `flutter.sdk=...` (this file is machine-local and is ignored by git)

### Find your Flutter SDK path (Windows)

Run:

```powershell
where flutter
```

If it prints something like `C:\src\flutter\bin\flutter.bat`, then your Flutter SDK path is `C:\src\flutter`.

### Create `android/local.properties`

Copy `android/local.properties.example` to `android/local.properties` and update the paths for your PC.

## Run

From the project root:

```powershell
flutter doctor
flutter pub get
flutter run
```

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.

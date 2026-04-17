# MR. SUGI — Office Cleanup Hero

Game HTML5 siap deploy ke Vercel + PWA shortcut di homescreen HP.

## File yang ada:
- `index.html` — game utama (all-in-one)
- `manifest.json` — PWA manifest (shortcut homescreen)
- `sw.js` — service worker (offline support)
- `icon-192.png` & `icon-512.png` — icon app
- `vercel.json` — config Vercel

## Cara Deploy ke Vercel:

### Langkah 1 — Upload ke GitHub
1. Buka github.com → New repository
2. Beri nama misal: `mr-sugi-game`
3. Upload semua file dari folder ini (drag & drop semua file)
4. Klik "Commit changes"

### Langkah 2 — Deploy ke Vercel
1. Buka vercel.com → Sign in with GitHub
2. Klik "Add New Project"
3. Pilih repo `mr-sugi-game`
4. Klik Deploy (tidak perlu setting apapun)
5. Selesai! Game live di URL Vercel

### Langkah 3 — Tambah ke Homescreen HP (PWA)
**Android (Chrome):**
1. Buka URL game di Chrome
2. Tap menu ⋮ → "Add to Home screen"
3. Ketuk "Add" → icon MR.SUGI muncul di homescreen

**iPhone (Safari):**
1. Buka URL game di Safari
2. Tap tombol Share (kotak dengan panah atas)
3. Pilih "Add to Home Screen"
4. Tap "Add" → icon MR.SUGI muncul di homescreen

Game akan terbuka fullscreen seperti aplikasi native!

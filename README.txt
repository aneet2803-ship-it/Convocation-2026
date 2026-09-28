GJIMT CONVOCATION 2026 – UPDATED GALLERY

This version contains 3 galleries:
1. Vice-Chancellor
2. Registrar
3. Meritorious Students

DUMMY IMAGES
Three dummy images are included in each gallery. Replace them with your original JPG/PNG images.

HOW TO REPLACE PHOTOS
1. Put VC photos in: images/vc/
2. Put Registrar photos in: images/registrar/
3. Put Meritorious Student photos in: images/meritorious/
4. Open manifest.js and replace the dummy filenames with the exact filenames of your photos.
5. Upload the complete gjimt_convocation_gallery folder to your GitHub repository.
6. Keep index.html, manifest.js, assets and images folders together.

DOWNLOAD PASSWORD
GJIMT@2026

IMPORTANT SECURITY NOTE
GitHub Pages is static public hosting. The JavaScript password prompt controls the page's Download buttons, but it does NOT make the underlying image URLs private or securely encrypted. Do not use this alone for genuinely confidential photographs.


V3 CHANGES
- Original photos now sit INSIDE a permanent branded orange/charcoal photo frame.
- The branded border remains visible even after dummy images are replaced.
- After a correct password, a single image download starts automatically.
- Download All attempts to download every image listed for the selected gallery after one correct password.
- Your browser may ask you to Allow multiple automatic downloads for the site. Choose Allow.

NOTE: Download All follows manifest.js. Every image you want downloaded must be listed there.


FINAL FIX
- Fixed manifest.js loading order/cache issue that could show 0 photographs even when filenames were present.
- Removed any empty gallery-data override from index.html.
- Image names remain hidden on gallery cards.
- Added test-manifest.html. Open it locally; it should display the arrays from manifest.js.
- Keep index.html and manifest.js in the same folder.


DOWNLOAD FIX
- Removed fetch/blob based downloading, which can fail when index.html is opened locally with file://.
- Correct password now triggers a direct browser download.
- Download All triggers direct downloads for every image listed in the selected gallery.
- Chrome may ask permission to allow multiple automatic downloads. Choose Allow.


FINAL RELIABLE DOWNLOAD FIX
- Individual Download now uses embedded file data, so it works even when index.html is opened locally with file://.
- After the correct password, the selected photograph downloads automatically.
- Download All now downloads ONE ZIP containing all available photographs in the selected gallery. This avoids Chrome blocking multiple automatic downloads.
- downloads-data.js contains the downloadable copies.
- If you replace/add photographs later, update manifest.js and run REBUILD_DOWNLOADS.py once before uploading the website.

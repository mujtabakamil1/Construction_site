# Image Setup Guide

## Folder Structure for Images

Place your construction images in:
```
static/images/
├── about-construction.jpg          (About Us section - 800x600px recommended)
├── project-1.jpg                   (Project 1 - 600x400px)
├── project-2.jpg                   (Project 2 - 600x400px)
├── project-3.jpg                   (Project 3 - 600x400px)
├── project-4.jpg                   (Project 4 - 600x400px)
└── gallery/                        (Optional - additional images)
    ├── construction-1.jpg
    ├── construction-2.jpg
    └── construction-3.jpg
```

## Where Images Will Appear

### 1. **About Us Section** (`about-construction.jpg`)
   - Location: Left side of About Us section
   - Size: 800px × 600px (or similar aspect ratio)
   - Type: Construction site photo or company headquarters
   - Purpose: Represents your company's work

### 2. **Projects/Legacy Section** (`project-1.jpg` through `project-4.jpg`)
   - Location: Top of each project card
   - Size: 600px × 400px (or similar aspect ratio)
   - Type: Photos of completed projects
   - Purpose: Visual showcase of your work

## Image Recommendations

### File Format
- **JPG/JPEG**: Best for photographs (smaller file size)
- **PNG**: Good for graphics with transparency
- **WebP**: Modern format with better compression

### File Size
- Keep images under 500KB each for better performance
- Use tools like TinyPNG or Compressor.io to optimize

### Naming Convention
- Use lowercase: `project-1.jpg` not `Project-1.JPG`
- Use hyphens: `about-construction.jpg` not `about_construction.jpg`
- No spaces in filenames

### Aspect Ratios
- About Us image: 4:3 ratio (800×600, 1200×900, etc.)
- Project images: 3:2 ratio (600×400, 900×600, etc.)

## How Images Work

1. **Image Not Found**: If an image doesn't exist, a purple placeholder with a building icon will show
2. **Hover Effect**: Images zoom slightly when you hover over them
3. **Responsive**: Images scale on mobile devices automatically
4. **Fallback**: If image fails to load, placeholder displays

## Steps to Add Your Images

1. **Create the folder** (already done):
   ```
   d:\Construction_site\static\images\
   ```

2. **Copy your images** to the folder:
   - Rename them to match the names above
   - Example: `your-photo.jpg` → `about-construction.jpg`

3. **Optional - Optimize images**:
   - Use online compressors to reduce file size
   - Keep aspect ratios correct

4. **Refresh browser** to see changes:
   - Press `Ctrl + F5` (hard refresh)
   - Or clear browser cache

## Example File Paths

Windows:
```
d:\Construction_site\static\images\about-construction.jpg
d:\Construction_site\static\images\project-1.jpg
d:\Construction_site\static\images\project-2.jpg
```

## Troubleshooting

### Images not showing?
1. Check file names match exactly (case-sensitive)
2. Make sure images are in `static/images/` folder
3. Refresh page (Ctrl + F5)
4. Check browser console for errors (F12)

### Images look blurry?
1. Use higher resolution images
2. Check if image is being stretched
3. Ensure aspect ratio is correct

### Images load slow?
1. Reduce file size using compression
2. Use WebP format for modern browsers
3. Consider resizing images to exact dimensions

---

**Ready?** Just copy your construction photos to `static/images/` folder with the recommended names! 📸

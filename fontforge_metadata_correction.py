#!/usr/bin/env python
# FontForge Python Script to Edit Font Metadata
# Usage: Open FontForge, load your font, then go to File > Execute Script
# and run this script

import fontforge

# Get the currently open font
font = fontforge.activeFont()

if font is None:
    print("Error: No font is currently open in FontForge!")
    print("Please open a font file first, then run this script.")
else:
    # ============================================================
    # EDIT THESE VALUES TO SET YOUR METADATA
    # ============================================================
    
    baseName = "RNX"
    family = "Pro"
    weight = "Regular"
    owner = "Aurora Foundry"
    url = "https://www.aurorafoundry.com"
    version = font.version
    year = "2025"
    vendorID = "ARUR"
    
    # ============================================================
    # COMPUTED VALUES (auto-generated from above)
    # ============================================================
    
    fontname = f'{baseName}{family}-{weight}'
    familyname = f'{baseName} {family}'
    fullname = f'{baseName} {family} {weight}'
    copyright = f"© {year} {owner}. All rights reserved."
    trademark = f"{baseName} {family} is a trademark of {owner}."
    manufacturer = owner
    designer = owner
    descriptor = owner
    vendorurl = url
    designerurl = url
    preferedFamily = f"{baseName} {family}"
    preferedStyles = weight
    uniqueID = f"{owner}: {fullname}: {year}"
    
    # ============================================================
    # DISPLAY CURRENT METADATA
    # ============================================================
    
    print("Current font metadata:")
    print("-" * 60)
    print(f"Family Name: {font.familyname}")
    print(f"Full Name: {font.fullname}")
    print(f"Font Name: {font.fontname}")
    print(f"Weight: {font.weight}")
    print(f"Copyright: {font.copyright}")
    print(f"Version: {font.version}")
    print("-" * 60)
    
    # ============================================================
    # APPLY NEW METADATA
    # ============================================================
    
    print("\nApplying new metadata...")
    
    # Basic font properties
    font.familyname = familyname
    font.fullname = fullname
    font.fontname = fontname
    font.weight = weight
    font.copyright = copyright
    font.version = version
    
    # Set OS/2 vendor ID
    font.os2_vendor = vendorID
    
    # Clear existing SFNT name table entries to avoid duplicates
    font.sfnt_names = ()
    
    # TTF/OTF Name Table entries (ID 0-19)
    font.appendSFNTName('English (US)', 'Copyright', copyright)
    font.appendSFNTName('English (US)', 'Family', familyname)
    font.appendSFNTName('English (US)', 'SubFamily', weight)
    font.appendSFNTName('English (US)', 'UniqueID', uniqueID)
    font.appendSFNTName('English (US)', 'Fullname', fullname)
    font.appendSFNTName('English (US)', 'Version', f'Version {version}')
    font.appendSFNTName('English (US)', 'PostScriptName', fontname)
    font.appendSFNTName('English (US)', 'Trademark', trademark)
    font.appendSFNTName('English (US)', 'Manufacturer', manufacturer)
    font.appendSFNTName('English (US)', 'Designer', designer)
    font.appendSFNTName('English (US)', 'Descriptor', descriptor)
    font.appendSFNTName('English (US)', 'Vendor URL', vendorurl)
    font.appendSFNTName('English (US)', 'Designer URL', designerurl)
    font.appendSFNTName('English (US)', 'Preferred Family', preferedFamily)
    font.appendSFNTName('English (US)', 'Preferred Styles', preferedStyles)
    
    # ============================================================
    # DISPLAY NEW METADATA
    # ============================================================
    
    print("\nNew metadata applied:")
    print("-" * 60)
    print(f"Family Name: {font.familyname}")
    print(f"Full Name: {font.fullname}")
    print(f"Font Name: {font.fontname}")
    print(f"Weight: {font.weight}")
    print(f"Copyright: {font.copyright}")
    print(f"Version: {font.version}")
    print("-" * 60)
    
    print("\n✓ Metadata update completed successfully!")
    print("\nNext steps:")
    print("1. Review the changes above")
    print("2. Save your font: File > Generate Fonts")
    print("   Or use: font.generate('output.ttf') in the script")
    print("\nNote: The font is modified in memory. Save to apply changes permanently.")

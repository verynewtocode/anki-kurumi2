# Kurumi Tokisaki Support Message Add-on

This repository contains a minimal Anki add-on that celebrates opening the
application with an encouraging message: "kurumi tokisaki supports passing of
actuarial practice CP1". The message appears in red text for five seconds as
soon as the Anki main window finishes loading.

## Add-on behaviour

The add-on hooks into `main_window_did_init` so the tooltip is shown immediately
after Anki finishes constructing the main window. The tooltip text is rendered
with inline HTML styling to force a red font colour and automatically disappears
after five seconds.

## File layout

```
kurumi_support_message/
├── __init__.py      # Add-on logic that triggers the tooltip on startup
└── manifest.json    # Metadata required by Anki's add-on packaging system
```

## Publishing the add-on to AnkiWeb

Follow these steps (based on the [official add-on writing documentation](https://addon-docs.ankiweb.net/))
to prepare and publish the add-on:

1. **Set your metadata**
   - Update `manifest.json` with the desired `version`, `mod` timestamp (Unix
     epoch in seconds), author information, and any additional metadata such as
     `homepage` or `tags`.
   - Review the human-friendly add-on name under the `name` key. This is what
     appears on AnkiWeb.
2. **Document the add-on**
   - Create a detailed `README.md` (this file) describing the add-on’s purpose,
     installation instructions, and change log.
   - Prepare screenshots or other media if you want to include them in your
     AnkiWeb listing.
3. **Bundle the add-on files**
   - Ensure only the files required for the add-on to run are included in the
     folder (see the next section for zipping instructions).
4. **Create or log in to an AnkiWeb account**
   - Navigate to [AnkiWeb Add-ons](https://ankiweb.net/shared/addons/) and sign in.
5. **Submit the package**
   - Click **Upload Add-on** and attach the zipped package produced in the next
     section.
   - Provide a descriptive title, summary, and full description.
   - Optionally include screenshots or additional documentation links.
6. **Maintain the listing**
   - When publishing updates, increment the `version`, update the `mod`
     timestamp, rebuild the ZIP archive, and upload the new package through the
     **Update** option on AnkiWeb.

## Creating the distributable ZIP

The add-on should be zipped so that the archive root contains the add-on
package directory (for this project, `kurumi_support_message`). On Linux or macOS
use the following command from the repository root:

```bash
zip -r kurumi_support_message.zip kurumi_support_message
```

On Windows using PowerShell:

```powershell
Compress-Archive -Path kurumi_support_message -DestinationPath kurumi_support_message.zip
```

After creating the archive, you can verify its structure:

```bash
unzip -l kurumi_support_message.zip
```

The output should list `kurumi_support_message/__init__.py` and
`kurumi_support_message/manifest.json`. This ZIP file is what you upload to
AnkiWeb or share with other users for manual installation.

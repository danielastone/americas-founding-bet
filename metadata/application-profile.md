# Metadata application profile

This project uses a deliberately small metadata profile. It is BIBFRAME-aligned but is not represented as official Library of Congress cataloging.

## Layers

| Layer | Purpose |
|---|---|
| Original archival metadata | Preserve the holding institution’s description and identifier |
| Normalized source register | Support project-wide search, citation, and validation |
| BIBFRAME-aligned export | Connect Works, Instances, Items, Agents, Places, and Topics |
| Claims register | Record what the project infers from each source |
| Analytical data | Record extracted measurements and transformations |

## Minimum source fields

- project source identifier;
- title;
- date;
- creator;
- holding institution;
- source type;
- repository identifier;
- stable landing page;
- theme;
- evidence role;
- BIBFRAME alignment;
- verification status; and
- notes.

## Core BIBFRAME alignment

| Project concept | Alignment |
|---|---|
| Intellectual creation | `bf:Work` |
| Edition or publication | `bf:Instance` |
| Specific held object | `bf:Item` |
| Person or organization | `bf:Agent` |
| Geographic subject | `bf:Place` |
| Topical subject | `bf:Topic` |
| Digitized representation | Electronic Instance or linked digital resource, depending on the source record |

## Archival constraint

Collection, series, folder, and item hierarchy must be retained separately. BIBFRAME must not flatten archival provenance.

## Identity rule

Records may be automatically linked only by stable institutional identifiers or verified authority URIs. Similar titles, names, dates, OCR text, or embeddings may generate candidate matches but cannot merge records without review.

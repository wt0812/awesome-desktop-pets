# Desktop Pet Builder Guide

This guide is a practical checklist for building a desktop pet or small overlay widget.

## Pick the Window Layer First

The hardest part is usually not the character. It is the window.

| Stack | Good for | Watch out |
|---|---|---|
| AppKit / Swift | polished macOS utilities, native menus, desktop-widget behavior | window levels, Spaces behavior, focus, sandbox rules |
| Qt / PyQt / PySide | cross-platform overlays, fast Python iteration | packaging, HiDPI, input transparency |
| Electron | web UI, Live2D, model-backed assistants | memory use, always-on-top behavior, system permissions |
| Unity / Godot | 2D/3D characters, rich animation | transparent windows and packaging are platform-specific |
| Browser widget | quick demos and embedded dashboards | not a true desktop pet unless wrapped |

## Interaction Rules

A good pet should feel present without getting in the way.

- Idle animation should be slow by default.
- Click-through should be explicit and reversible.
- Dragging should be smooth and predictable.
- The pet should not steal keyboard focus unless the user asks for input.
- If it can read the screen or files, the permission boundary must be obvious.

## Character Pack Shape

A maintainable character pack usually has:

```text
character/
  static.png
  blink.png
  walk.gif
  sleep.gif
  config.json
```

Useful fields:

- default size
- anchor point
- idle animation interval
- emotion/state names
- optional sounds
- optional local-model prompt persona

## AI Pet Safety Baseline

If a pet uses a local or cloud model, document:

- model backend
- whether it sends network requests
- whether it reads screen content
- whether it stores memory
- how to delete conversation state

The best AI desktop pets are boring about privacy and playful about the character.

## Feature Ideas That Age Well

- character pack importer
- state machine for idle / sleep / focus / work modes
- local notifications that do not feel like alarms
- simple plugin API for desktop events
- energy / mood tied to explicit user actions
- optional integration with coding agents, calendars, or notes

## Common Anti-Patterns

- too many animations per minute
- hidden always-on-top behavior
- modal dialogs from a pet window
- unclear close / pause controls
- AI features that require a cloud API before the basic pet works

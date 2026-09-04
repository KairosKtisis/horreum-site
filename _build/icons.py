# Line icons for the feature cards (24-box, stroked, inherit color).
def _svg(paths): return '<svg viewBox="0 0 24 24" aria-hidden="true">' + paths + '</svg>'
ICON = {
  "ledger":  _svg('<path d="M5 4h11l3 3v13H5z"/><path d="M8 9h8M8 13h8M8 17h5"/>'),
  "label":   _svg('<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3h-3zM18 18h3v3h-3zM18 14h3M14 18v3"/>'),
  "spot":    _svg('<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M4 9h16M4 15h16M9 3v18"/>'),
  "find":    _svg('<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.2-4.2"/><path d="M11 8v3l2 1.5"/>'),
  "roles":   _svg('<circle cx="9" cy="8" r="3.2"/><path d="M3.5 19a5.5 5.5 0 0 1 11 0"/><path d="M16 4.5a3 3 0 0 1 0 6"/><path d="M17 13.5a5.5 5.5 0 0 1 3.5 5.5"/>'),
  "log":     _svg('<path d="M4 6h16M4 12h16M4 18h10"/><circle cx="19" cy="18" r="2"/>'),
  "notes":   _svg('<path d="M12 3c-1.5 3-5 5-5 9a5 5 0 0 0 10 0c0-4-3.5-6-5-9z"/><path d="M12 21v-4"/>'),
  "brand":   _svg('<path d="M4 20l8-16 8 16"/><path d="M8 13h8"/>'),
  "globe":   _svg('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'),
  "history": _svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
  "star":    _svg('<path d="M12 3.5l2.6 5.5 6 .7-4.4 4.1 1.2 5.9L12 16.8l-5.4 2.9 1.2-5.9L3.4 9.7l6-.7z"/>'),
  "phone":   _svg('<rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18h2"/>'),
  "shield":  _svg('<path d="M12 3l7 3v5c0 5-3.5 8-7 10-3.5-2-7-5-7-10V6z"/><path d="M9 12l2 2 4-4"/>'),
  "card":    _svg('<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18M7 15h4"/>'),
  "import":  _svg('<path d="M12 4v11M8 11l4 4 4-4"/><path d="M4 19h16"/>'),
  "chat":    _svg('<path d="M4 5h16v11H9l-5 4z"/>'),
  "bottle":  _svg('<path d="M10 3h4v4l2 3v11H8V10l2-3z"/><path d="M8 14h8"/>'),
  "check":   _svg('<path d="M5 12l4 4L19 7"/>'),
}

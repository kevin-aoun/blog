---
title: Graph
permalink: /graph/
---

# Graph

<p class="graph-hint">Notes cluster around their topic. Lines are <code>[[wikilinks]]</code> between notes. Click a node to open it.</p>

<div id="graph" class="graph"></div>

<script src="{{ '/assets/js/force-graph.min.js' | relative_url }}"></script>
<script>
  (function () {
    var el = document.getElementById('graph');
    if (!el) return;
    function msg(t) { el.innerHTML = '<p class="graph-msg">' + t + '</p>'; }
    if (typeof ForceGraph === 'undefined') { msg('Graph library failed to load (force-graph.min.js).'); return; }
    var TOPIC = { tech: '#3b82f6', legacy: '#e0902b', philosophy: '#3aa35a', psychology: '#a78bfa' };
    function tok(v) { return getComputedStyle(document.documentElement).getPropertyValue(v).trim() || '#888'; }
    function catColor(c) { return TOPIC[c] || tok('--muted'); }

    fetch('{{ "/notes.json" | relative_url }}')
      .then(function (r) { if (!r.ok) throw new Error('notes.json returned HTTP ' + r.status); return r.text(); })
      .then(function (txt) {
        var notes;
        try { notes = JSON.parse(txt); }
        catch (e) { msg('notes.json is not valid JSON (' + e.message + '). See the console.'); console.error('Raw notes.json:\n' + txt); return; }
        if (!Array.isArray(notes) || !notes.length) { msg('No notes to graph yet.'); return; }

        var nodes = [], links = [], byTitle = {}, cats = {};
        notes.forEach(function (n) {
          var cat = (n.category || 'Notes'), key = cat.toLowerCase();
          var node = { id: n.title, url: n.url, cat: key, kind: 'note' };
          nodes.push(node); byTitle[n.title] = node; cats[key] = cat;
        });
        Object.keys(cats).forEach(function (key) {
          nodes.push({ id: 'cat:' + key, label: cats[key], cat: key, kind: 'hub' });
        });
        notes.forEach(function (n) {
          var key = (n.category || 'Notes').toLowerCase();
          links.push({ source: n.title, target: 'cat:' + key, kind: 'cluster' });
          (n.links || []).forEach(function (t) {
            if (byTitle[t]) links.push({ source: n.title, target: t, kind: 'wiki' });
          });
        });

        var fg = ForceGraph()(el)
          .graphData({ nodes: nodes, links: links })
          .backgroundColor('rgba(0,0,0,0)')
          .linkColor(function (l) { return l.kind === 'wiki' ? tok('--muted') : tok('--border'); })
          .linkWidth(function (l) { return l.kind === 'wiki' ? 1.6 : 0.6; })
          .onNodeClick(function (n) { if (n.url) window.location.href = n.url; })
          .nodeCanvasObject(function (node, ctx, scale) {
            var r = node.kind === 'hub' ? 6 : 4;
            ctx.beginPath();
            ctx.arc(node.x, node.y, r, 0, 2 * Math.PI);
            ctx.fillStyle = catColor(node.cat);
            ctx.globalAlpha = node.kind === 'hub' ? 0.35 : 1;
            ctx.fill();
            ctx.globalAlpha = 1;
            // Fade labels out as you zoom out, to avoid clutter.
            var la = Math.max(0, Math.min(1, (scale - 0.8) / 0.5));
            if (la < 0.03) return;
            var label = node.kind === 'hub' ? node.label : node.id;
            ctx.font = (node.kind === 'hub' ? 12 : 10) / scale + 'px Geist, sans-serif';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'top';
            ctx.globalAlpha = la;
            ctx.fillStyle = node.kind === 'hub' ? catColor(node.cat) : tok('--foreground');
            ctx.fillText(label, node.x, node.y + r + 2);
            ctx.globalAlpha = 1;
          })
          .nodePointerAreaPaint(function (node, color, ctx) {
            ctx.fillStyle = color;
            ctx.beginPath();
            ctx.arc(node.x, node.y, 8, 0, 2 * Math.PI);
            ctx.fill();
          });

        // Keep every node (including a dragged one) inside a bounded box so
        // nothing can be flung off the frame and vanish.
        var BX = 240, BY = 165;
        function clamp(v, m) { return Math.max(-m, Math.min(m, v)); }
        fg.d3Force('bound', function () {
          nodes.forEach(function (n) {
            n.x = clamp(n.x, BX); n.y = clamp(n.y, BY);
            if (n.fx != null) n.fx = clamp(n.fx, BX);
            if (n.fy != null) n.fy = clamp(n.fy, BY);
          });
        });
        fg.minZoom(0.6).maxZoom(8);
        var fitted = false;
        fg.onEngineStop(function () { if (!fitted) { fitted = true; fg.zoomToFit(400, 30); } });

        function resize() { fg.width(el.clientWidth).height(el.clientHeight); }
        resize();
        window.addEventListener('resize', resize);
      })
      .catch(function (e) { msg('Could not load notes.json: ' + e.message); console.error(e); });
  })();
</script>

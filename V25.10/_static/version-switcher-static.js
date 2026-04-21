(function () {
  const VERSIONS = [
    { key: "default", label: "V25.04" },
    { key: "V25.10", label: "V25.10" }
  ];

  function logWarn(e) {
    try { console.warn("[version-switcher]", e); } catch (_) {}
  }

  function getContentRootPath() {
    // Sphinx 在 <html> 上有 data-content_root，例如 "./" 或 "../"
    const html = document.documentElement;
    const cr = html && html.getAttribute("data-content_root");
    return (cr && cr.trim()) ? cr.trim() : "./";
  }

  function urlDir(u) {
    const x = String(u).split("#")[0].split("?")[0];
    return x.substring(0, x.lastIndexOf("/") + 1); // endswith /
  }

  function getVersionRootUrl() {
    // 当前“版本根目录”的绝对 URL
    // default 页面：file:///.../show_html/index.html + "./" => file:///.../show_html/
    // V25.10 页面：file:///.../show_html/V25.10/sub/a.html + "../../" (通常) => file:///.../show_html/V25.10/
    const base = urlDir(location.href);
    const cr = getContentRootPath();
    return new URL(cr, base).toString();
  }

  function getSiteRootUrl(versionRootUrl) {
    // 站点总根：放 go.html 的目录
    // 如果当前是 .../V25.10/，就回到上一级
    const u = String(versionRootUrl);
    const m = u.match(/^(.*\/)V\d+\.\d+\/$/);
    if (m) return m[1];
    return u; // default 本身就是站点根
  }

  function detectCurrent(versionRootUrl) {
    // 通过版本根路径判断是否在 V25.10
    return /\/V25\.10\/$/.test(versionRootUrl) ? "V25.10" : "default";
  }

  function inject() {
    try {
      const versionRoot = getVersionRootUrl();
      const siteRoot = getSiteRootUrl(versionRoot);
      const cur = detectCurrent(versionRoot);

      const box = document.createElement("div");
      box.id = "docs-version-switcher";

      const label = document.createElement("label");
      label.textContent = "Version:";

      const select = document.createElement("select");
      for (const v of VERSIONS) {
        const opt = document.createElement("option");
        opt.value = v.key;
        opt.textContent = v.label;
        opt.selected = (v.key === cur);
        select.appendChild(opt);
      }

      select.addEventListener("change", () => {
        const t = select.value; // default or V25.10
        if (t === cur) return;

        const go = siteRoot + "go.html";
        location.href = go + "?to=" + encodeURIComponent(t);
      });

      box.appendChild(label);
      box.appendChild(select);
      document.body.appendChild(box);
    } catch (e) {
      logWarn(e);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", inject);
  } else {
    inject();
  }
})();
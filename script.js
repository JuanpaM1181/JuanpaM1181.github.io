const GITHUB_USER = "JuanpaM1181";
const REPOS_URL = `https://api.github.com/users/${GITHUB_USER}/repos?sort=updated&per_page=20`;

const LANG_COLORS = {
  "C#": "#178600",
  "JavaScript": "#f1e05a",
  "Vue": "#41b883",
  "Python": "#3572A5",
  "Game Maker Language": "#8cdcda",
  "HTML": "#e34c26",
  "CSS": "#563d7c",
  "Shell": "#89e051",
};

async function fetchRepos() {
  const container = document.getElementById("repos");

  try {
    const res = await fetch(REPOS_URL);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const repos = await res.json();

    if (repos.length === 0) {
      container.innerHTML = '<div class="repo-error">No hay repositorios públicos.</div>';
      return;
    }

    const featured = repos.filter(r => !r.fork && r.stargazers_count > 0);
    const rest = repos.filter(r => !r.fork && r.stargazers_count === 0);
    const ordered = [...featured, ...rest].slice(0, 12);

    container.innerHTML = ordered.map(repo => {
      const lang = repo.language || "";
      const color = LANG_COLORS[lang] || "#6e7681";
      const desc = repo.description || "Sin descripción";
      const stars = repo.stargazers_count;

      return `
        <a href="${repo.html_url}" target="_blank" rel="noopener" class="repo-card">
          <div class="repo-name">${repo.name}</div>
          <div class="repo-desc">${escHtml(desc)}</div>
          <div class="repo-meta">
            ${lang ? `<span><span class="repo-lang" style="background:${color}"></span>${escHtml(lang)}</span>` : ""}
            ${stars > 0 ? `<span>★ ${stars}</span>` : ""}
          </div>
        </a>
      `;
    }).join("");
  } catch (err) {
    container.innerHTML = `<div class="repo-error">Error al cargar repos: ${err.message}</div>`;
  }
}

function escHtml(s) {
  const div = document.createElement("div");
  div.textContent = s;
  return div.innerHTML;
}

fetchRepos();

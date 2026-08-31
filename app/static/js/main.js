/**
 * Main application UI controller
 */

document.addEventListener('DOMContentLoaded', () => {
  updateNavbar();
});

function updateNavbar() {
  const authNav = document.getElementById('nav-auth-section');
  if (!authNav) return;

  const isAuth = isAuthenticated();
  const user = getStoredUser();

  if (isAuth) {
    const displayName = user ? (user.full_name || user.username) : 'حسابي';
    authNav.innerHTML = `
      <span style="color: var(--text-muted); font-size: 0.9rem;">مرحباً، <strong style="color: var(--text-main);">${displayName}</strong></span>
      <a href="/" class="btn btn-secondary" style="padding: 0.5rem 1rem;">الرئيسية</a>
      <button onclick="logout()" class="btn btn-danger" style="padding: 0.5rem 1rem;">خروج</button>
    `;
  } else {
    authNav.innerHTML = `
      <a href="/login" class="btn btn-secondary" style="padding: 0.5rem 1rem;">تسجيل الدخول</a>
      <a href="/register" class="btn btn-primary" style="padding: 0.5rem 1rem;">حساب جديد</a>
    `;
  }
}

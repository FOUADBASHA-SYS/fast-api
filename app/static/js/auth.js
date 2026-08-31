/**
 * Authentication & API Helper Library
 */

const AUTH_KEY = 'fastapi_auth_token';
const USER_KEY = 'fastapi_auth_user';

// Token Storage
function setAuthToken(token, user = null) {
  localStorage.setItem(AUTH_KEY, token);
  document.cookie = `access_token=Bearer ${token}; path=/; max-age=${60 * 60 * 24}; SameSite=Lax`;
  if (user) {
    localStorage.setItem(USER_KEY, JSON.stringify(user));
  }
}

function getAuthToken() {
  return localStorage.getItem(AUTH_KEY);
}

function getStoredUser() {
  const userStr = localStorage.getItem(USER_KEY);
  try {
    return userStr ? JSON.parse(userStr) : null;
  } catch (e) {
    return null;
  }
}

function removeAuthToken() {
  localStorage.removeItem(AUTH_KEY);
  localStorage.removeItem(USER_KEY);
  document.cookie = "access_token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC;";
}

function isAuthenticated() {
  return !!getAuthToken();
}

function logout() {
  removeAuthToken();
  window.location.href = '/login';
}

/**
 * Universal Fetch wrapper with Bearer token & JSON support
 */
async function apiRequest(endpoint, options = {}) {
  const token = getAuthToken();
  const headers = {
    'Content-Type': 'application/json',
    ...(options.headers || {})
  };

  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  const config = {
    ...options,
    headers
  };

  const response = await fetch(endpoint, config);
  const data = await response.json().catch(() => null);

  if (!response.ok) {
    const errorMsg = data && (data.detail || data.message) ? data.detail || data.message : 'حدث خطأ في الاتصال بالسيرفر';
    throw new Error(errorMsg);
  }

  return data;
}

/**
 * Helper to display alerts in cards
 */
function showAlert(elementId, message, type = 'error') {
  const alertEl = document.getElementById(elementId);
  if (!alertEl) return;

  alertEl.className = `alert alert-${type}`;
  alertEl.innerHTML = `
    <span>${type === 'error' ? '⚠️' : '✅'}</span>
    <div>${message}</div>
  `;
  alertEl.style.display = 'flex';
}

function hideAlert(elementId) {
  const alertEl = document.getElementById(elementId);
  if (alertEl) {
    alertEl.style.display = 'none';
  }
}

export const FAKE_SESSION_KEY = "microprelegal.fake-session";

export type FakeSession = {
  email: string;
  name: string;
};

function isBrowser() {
  return typeof window !== "undefined";
}

export function readSession(): FakeSession | null {
  if (!isBrowser()) {
    return null;
  }

  const rawValue = window.localStorage.getItem(FAKE_SESSION_KEY);

  if (!rawValue) {
    return null;
  }

  try {
    return JSON.parse(rawValue) as FakeSession;
  } catch {
    window.localStorage.removeItem(FAKE_SESSION_KEY);
    return null;
  }
}

export function writeSession(session: FakeSession) {
  window.localStorage.setItem(FAKE_SESSION_KEY, JSON.stringify(session));
}

export function clearSession() {
  if (!isBrowser()) {
    return;
  }

  window.localStorage.removeItem(FAKE_SESSION_KEY);
}

export const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api/v1'

export async function apiGet<T>(path: string): Promise<T> {
  const res = await fetch(`${API_URL}${path}`)
  if (!res.ok) throw new Error(`GET ${path} failed: ${res.status}`)
  return (await res.json()) as T
}

import { useEffect, useState } from 'react'

const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api/v1'

export default function App() {
  const [message, setMessage] = useState<string>('')

  useEffect(() => {
    fetch(`${API_URL}/hello`)
      .then((r) => r.json())
      .then((data) => setMessage(data.message ?? JSON.stringify(data)))
      .catch((e) => setMessage(`Error: ${String(e)}`))
  }, [])

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="p-8 rounded-lg shadow bg-white space-y-4">
        <h1 className="text-2xl font-bold">Retail AI Frontend</h1>
        <p className="text-gray-700">Backend says: {message || 'Loading...'}</p>
        <div className="text-sm text-gray-500">API: {API_URL}</div>
      </div>
    </div>
  )
}

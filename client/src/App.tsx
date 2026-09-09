import { useState } from "react";
import "./App.css";

type GameState = {
  dice: number[];
  rolls_left: number;
  total_score: number;
};

function App() {
  const [game, setGame] = useState<GameState | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function loadPreview() {
    setLoading(true);
    setError("");

    try {
      const response = await fetch("/api/preview");

      if (!response.ok) {
        throw new Error("Could not load the game.");
      }

      const data: GameState = await response.json();
      setGame(data);
    } catch {
      setError("Could not load the preview. Check that Flask is running.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-800 p-8 text-slate-50">
      <h1 className="mb-6 text-3xl font-bold">Yahtzee Solver</h1>

      <button
        onClick={loadPreview}
        disabled={loading}
        className="rounded bg-blue-600 px-4 py-2 disabled:opacity-50"
      >
        {loading ? "Loading..." : "Preview a roll"}
      </button>

      {error && (
        <p role="alert" className="mt-4 text-red-300">
          {error}
        </p>
      )}

      {game && (
        <section className="mt-6">
          <div className="mb-4 flex gap-3">
            {game.dice.map((die, index) => (
              <div
                key={index}
                className="flex h-12 w-12 items-center justify-center rounded bg-white text-2xl font-bold text-slate-900"
              >
                {die}
              </div>
            ))}
          </div>

          <p>Rolls left: {game.rolls_left}</p>
          <p>Total score: {game.total_score}</p>
        </section>
      )}
    </main>
  );
}

export default App;

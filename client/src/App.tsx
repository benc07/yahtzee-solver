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
  const [keep, setKeep] = useState<boolean[]>([
    false,
    false,
    false,
    false,
    false,
  ]);

  async function updateGame(path: string) {
    setLoading(true);
    setError("");

    try {
      const response = await fetch(path, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(path === "/api/game/roll" ? { keep } : {}),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error ?? "Request failed.");
      }

      setGame(data);
      if (path === "/api/game") {
        setKeep([false, false, false, false, false]);
      }
    } catch (error) {
      setError(
        error instanceof Error ? error.message : "Could not reach the server.",
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-800 p-8 text-slate-50">
      <h1 className="mb-6 text-3xl font-bold">Yahtzee Solver</h1>

      <div className="flex gap-3">
        <button
          onClick={() => updateGame("/api/game")}
          disabled={loading}
          className="rounded bg-blue-600 px-4 py-2 disabled:opacity-50"
        >
          New game
        </button>

        <button
          onClick={() => updateGame("/api/game/roll")}
          disabled={loading || !game || game.rolls_left === 0}
          className="rounded bg-green-600 px-4 py-2 disabled:opacity-50"
        >
          Roll
        </button>
      </div>

      {loading && <p className="mt-4">Loading...</p>}

      {error && (
        <p role="alert" className="mt-4 text-red-300">
          {error}
        </p>
      )}

      {game && (
        <section className="mt-6">
          <div className="mb-4 flex gap-3">
            {game.dice.map((die, index) => (
              <button
                key={index}
                aria-label={`Die ${index + 1}: ${die}`}
                aria-pressed={keep[index]}
                disabled={
                  loading || game.rolls_left === 3 || game.rolls_left === 0
                }
                onClick={() =>
                  setKeep((previous) =>
                    previous.map((held, i) => (i === index ? !held : held)),
                  )
                }
                className={`flex h-16 w-16 flex-col items-center justify-center rounded font-bold ${
                  keep[index]
                    ? "bg-amber-300 text-slate-900"
                    : "bg-white text-slate-900"
                }`}
              >
                <span className="text-2xl">{die}</span>
                <span className="text-xs">{keep[index] ? "Held" : "Hold"}</span>
              </button>
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

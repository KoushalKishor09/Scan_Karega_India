import ImageUpload from "./components/ImageUpload/ImageUpload";
import "./styles.css";

export default function App() {
  return (
    <main className="app-shell">
      <section className="hero">
        <p className="eyebrow">Scan Karega India</p>
        <h1>Food label analysis, wired up locally.</h1>
        <p className="subtitle">
          Upload a packaged food label and get a structured extraction with a simple health score.
        </p>
      </section>

      <section className="panel">
        <ImageUpload />
      </section>
    </main>
  );
}

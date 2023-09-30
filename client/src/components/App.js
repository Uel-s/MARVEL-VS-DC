import { Routes, Route } from "react-router-dom";
import Header from "./Header";
import Hero from "./Hero";
import Home from "./Home";
import HeroPowerForm from "./HeroPowerForm";
import Power from "./Power";
import PowerEditForm from "./PowerEditForm";

function App() {
  return (
    <div>
      <Header />
      <main>
        <Routes>
          <Route element={<HeroPowerForm />} exact path="/hero_powers/new" />

          <Route element={<PowerEditForm />} exact path="/powers/:id/edit" />

          <Route element={<Power />} exact path="/powers/:id" />

          <Route element={<Hero />} exact path="/heroes/:id" />

          <Route element={<Home />} exact path="/" />
        </Routes>
      </main>
    </div>
  );
}

export default App;

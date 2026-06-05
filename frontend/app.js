import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

import { Bar } from "react-chartjs-2";

import { supabase } from "./supabaseClient";
import Auth from "./Auth";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function App() {
  const [user, setUser] = useState(null);

  const [subject, setSubject] = useState("");
  const [gradeLevel, setGradeLevel] = useState("");
  const [topic, setTopic] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const [shareLink, setShareLink] = useState("");

  const [stats, setStats] = useState({
    total_assessments: 0,
    total_questions: 0,
    success_rate: 0,
  });

  const [recent, setRecent] = useState([]);
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    const getUser = async () => {
      const { data } = await supabase.auth.getUser();
      setUser(data?.user || null);
    };

    getUser();
  }, []);

  const loadStats = async () => {
    try {
      const statsRes = await axios.get(
        "https://educational-assessment-creator.onrender.com/stats"
      );

      const recentRes = await axios.get(
        "https://educational-assessment-creator.onrender.com/assessments"
      );

      setStats(statsRes.data);
      setRecent(recentRes.data.slice(0, 5));

      setChartData({
        labels: ["Assessments", "Questions", "Success Rate"],
        datasets: [
          {
            label: "AI Analytics",
            data: [
              statsRes.data.total_assessments,
              statsRes.data.total_questions,
              statsRes.data.success_rate,
            ],
            backgroundColor: ["#4f46e5", "#06b6d4", "#22c55e"],
          },
        ],
      });
    } catch (err) {
      console.log(err.message);
    }
  };

  useEffect(() => {
    if (user) loadStats();
  }, [user]);

  const createAssessment = async () => {
    if (!subject || !gradeLevel || !topic) {
      alert("Please fill all fields");
      return;
    }

    setLoading(true);

    try {
      const response = await axios.post(
        "https://educational-assessment-creator.onrender.com/create-assessment",
        {
          subject,
          grade_level: parseInt(gradeLevel),
          topic,
        }
      );

      setResult(response.data);

      // 🔥 SHARE LINK
      setShareLink(
        `${window.location.origin}/share/${response.data.share_id}`
      );

      loadStats();

      setSubject("");
      setGradeLevel("");
      setTopic("");
    } catch (error) {
      alert("Error: " + error.message);
    }

    setLoading(false);
  };

  const logout = async () => {
    await supabase.auth.signOut();
    setUser(null);
  };

  if (!user) return <Auth setUser={setUser} />;

  return (
    <div className="App">

      <div className="header">
        <h1>🚀 AI Assessment Creator</h1>
        <p>Welcome {user.email}</p>
        <button onClick={logout}>Logout</button>
      </div>

      <div className="stats">
        <div className="card">
          <h2>{stats.total_assessments}</h2>
        </div>
        <div className="card">
          <h2>{stats.total_questions}</h2>
        </div>
        <div className="card">
          <h2>{stats.success_rate}%</h2>
        </div>
      </div>

      {chartData && (
        <div style={{ width: "600px", margin: "40px auto" }}>
          <Bar data={chartData} />
        </div>
      )}

      <div className="form">
        <h2>Create Assessment</h2>

        <input value={subject} onChange={(e) => setSubject(e.target.value)} placeholder="Subject" />
        <input value={gradeLevel} onChange={(e) => setGradeLevel(e.target.value)} placeholder="Grade Level" />
        <input value={topic} onChange={(e) => setTopic(e.target.value)} placeholder="Topic" />

        <button onClick={createAssessment} disabled={loading}>
          {loading ? "Generating..." : "Create Assessment"}
        </button>
      </div>

      {/* 🔗 SHARE BOX */}
      {shareLink && (
        <div className="shareBox">
          <h3>Share Link</h3>
          <input value={shareLink} readOnly />

          <button onClick={() => navigator.clipboard.writeText(shareLink)}>
            Copy
          </button>

          <button onClick={() => window.open(shareLink, "_blank")}>
            Open
          </button>
        </div>
      )}

      {result && (
        <div className="result">
          <h2>Generated Questions</h2>

          {result.questions.map((q, i) => (
            <div key={i}>
              <h4>Q{q.id}</h4>
              <p>{q.question}</p>
            </div>
          ))}
        </div>
      )}

      <div className="result">
        <h2>Recent</h2>

        {recent.map((item, i) => (
          <div key={i}>
            <h4>{item.subject}</h4>
          </div>
        ))}
      </div>

    </div>
  );
}

export default App;
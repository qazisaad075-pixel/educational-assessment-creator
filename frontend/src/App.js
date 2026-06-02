import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [subject, setSubject] = useState('');
  const [gradeLevel, setGradeLevel] = useState('');
  const [topic, setTopic] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const createAssessment = async () => {
    setLoading(true);
    try {
      const response = await axios.post('https://educational-assessment-creator-production.up.railway.app/create-assessment', {
        subject: subject,
        grade_level: parseInt(gradeLevel),
        topic: topic
      });
      setResult(response.data);
    } catch (error) {
      alert('Error: ' + error.message);
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>Educational Assessment Creator</h1>

      <div className="form">
        <input
          placeholder="Subject (e.g. Mathematics)"
          value={subject}
          onChange={(e) => setSubject(e.target.value)}
        />
        <input
          placeholder="Grade Level (e.g. 9)"
          value={gradeLevel}
          onChange={(e) => setGradeLevel(e.target.value)}
        />
        <input
          placeholder="Topic (e.g. Algebra)"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
        />
        <button onClick={createAssessment} disabled={loading}>
          {loading ? 'Creating...' : 'Create Assessment'}
        </button>
      </div>

      {result && (
        <div className="result">
          <h2>Assessment Created!</h2>

          <h3>Learning Objectives</h3>
          <ul>
            {result.standards.objectives.map((obj, i) => (
              <li key={i}>{obj}</li>
            ))}
          </ul>

          <h3>Questions</h3>
          {result.questions.map((q, i) => (
            <div key={i} className="question">
              <p><strong>Q{q.id}:</strong> {q.question}</p>
              <p>Type: {q.type} | Difficulty: {q.difficulty} | Points: {q.points}</p>
            </div>
          ))}

          <h3>Analytics</h3>
          <p>Total Questions: {result.analytics.total_questions}</p>
          <p>Total Points: {result.analytics.total_points}</p>
        </div>
      )}
    </div>
  );
}

export default App;
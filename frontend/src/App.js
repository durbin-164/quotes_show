import React, { useEffect, useState } from 'react';

function App() {
  const [quote, setQuote] = useState('');
  const [source, setSource] = useState('');

  useEffect(() => {
    fetchQuote();
  }, []);

  const fetchQuote = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/quote');
      const data = await response.json();
      setQuote(data.quote);
      setSource(data.source);
    } catch (error) {
      console.error('Error fetching quote:', error);
    }
  };

  const quoteStyle = {
    textAlign: 'center',
    fontSize: '32px',
    fontWeight: 'bold',
    margin: '20px',
    color: source === 'Cache' ? '#00B894' : '#FF33A2',
  };

  const sourceStyle = {
    fontSize: '18px',
    fontStyle: 'italic',
    color: source === 'Cache' ? '#00B894' : '#FF33A2',
    textAlign: 'center',
  };

  const buttonStyle = {
    display: 'block',
    margin: '40px auto',
    padding: '12px 24px',
    fontSize: '20px',
    backgroundColor: '#3498DB',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
  };


  return (
    <div className="App" style={{ backgroundColor: '#FADBD8', minHeight: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <div>
        <h1 style={{ textAlign: 'center', fontSize: '48px', fontFamily: 'Arial', fontWeight: 'bold', color: '#AC33FF', margin: '20px' }}>Daily Inspiration</h1>
        <h1 style={quoteStyle}>{quote}</h1>
        <p style={sourceStyle}>Source: {source}</p>
        <p style={{ fontSize: '18px', color: '#3498DB', margin: '40px', textAlign: 'center' }}>Discover new insights, find motivation, and embrace the power of quotes in your daily life. Let inspiration guide your journey.</p>
        <button onClick={fetchQuote} style={buttonStyle}>Get Another Quote</button>
      </div>
    </div>
  );
}

export default App;

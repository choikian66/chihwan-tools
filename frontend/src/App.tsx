import { Routes, Route, NavLink, Navigate } from 'react-router-dom';
import BranchDiagnosis from './pages/BranchDiagnosis';
import ManualChat from './pages/ManualChat';

const NAV_STYLE: React.CSSProperties = {
  display: 'flex',
  gap: 0,
  borderBottom: '1px solid var(--border-primary)',
  background: 'white',
  padding: '0 24px',
};

const LINK_BASE: React.CSSProperties = {
  padding: '14px 18px',
  fontSize: 14,
  fontWeight: 600,
  color: 'var(--text-tertiary)',
  textDecoration: 'none',
  borderBottom: '2px solid transparent',
  marginBottom: -1,
  whiteSpace: 'nowrap',
};

export default function App() {
  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <nav style={NAV_STYLE}>
        <NavLink
          to="/diagnosis"
          style={({ isActive }) => ({
            ...LINK_BASE,
            color: isActive ? '#5B5FC7' : 'var(--text-tertiary)',
            borderBottomColor: isActive ? '#5B5FC7' : 'transparent',
          })}
        >
          80점 경영 진단
        </NavLink>
        <NavLink
          to="/manual"
          style={({ isActive }) => ({
            ...LINK_BASE,
            color: isActive ? '#5B5FC7' : 'var(--text-tertiary)',
            borderBottomColor: isActive ? '#5B5FC7' : 'transparent',
          })}
        >
          경영 매뉴얼 챗봇
        </NavLink>
      </nav>

      <main style={{ flex: 1, padding: '24px', overflowY: 'auto' }}>
        <Routes>
          <Route path="/" element={<Navigate to="/diagnosis" replace />} />
          <Route path="/diagnosis" element={<BranchDiagnosis />} />
          <Route path="/manual" element={<ManualChat />} />
        </Routes>
      </main>
    </div>
  );
}

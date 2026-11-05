import { useState, useCallback } from 'react'
import Sidebar from './components/Sidebar.jsx'
import Header from './components/Header.jsx'
import MissionControl from './components/MissionControl.jsx'
import FireRiskOverview from './components/FireRiskOverview.jsx'
import ResearchExplorer from './components/ResearchExplorer.jsx'
import MissionInsights from './components/MissionInsights.jsx'
import SpacecraftOverview from './components/SpacecraftOverview.jsx'
import EnvironmentExplorer from './components/EnvironmentExplorer.jsx'
import DataAnalytics from './components/DataAnalytics.jsx'
import HabitatSafetyAdvisor from './components/HabitatSafetyAdvisor.jsx'
import AIAgents from './components/AIAgents.jsx'
import BottomDashboards from './components/BottomDashboards.jsx'
import PageView from './components/PageView.jsx'
import { X } from 'lucide-react'
export default function App() {
 const [page,setPage]=useState('home'),[modal,setModal]=useState(null),[toast,setToast]=useState('')
 const openDetails=useCallback((title,body)=>setModal({title,body}),[])
 const notify=useCallback(msg=>{setToast(msg);setTimeout(()=>setToast(''),2600)},[])
 return <div className="app"><Sidebar page={page} onNavigate={setPage}/><main className="content">
 {page==='home'?<><section className="hero home-hero"><img className="hero-bg" src="/images/orbital-bg.webp" alt="Astronaut floating above a planet in space"/><div className="hero-shade"/><Header/><div className="home-copy"><span className="eyebrow"><i className="pulse-dot"/> SPACE FIRE INTELLIGENCE PLATFORM</span><h1>Protecting life<br/>beyond <em>Earth.</em></h1><p>Intelligent fire prediction and safety support for the next generation of space habitats.</p><div className="home-actions"><button onClick={()=>setPage('agent1')}>Explore Fire Predictor <span>↗</span></button><span>ORBITAL SI · MISSION CONTROL</span></div></div><div className="hero-caption">DEEP SPACE ENVIRONMENT <span>•</span> ORBITAL MONITORING</div></section>
 <div className="home-section-head"><div><span className="eyebrow">MISSION OVERVIEW</span><h2>Mission control center</h2></div><span className="tag-muted">DEMO DATA · ORBIT-07</span></div>
 <section className="home-overview"><div className="overview-left panel"><MissionControl/></div><FireRiskOverview/></section>
 <div className="row row2 home-row"><ResearchExplorer onDetails={openDetails}/><MissionInsights/><SpacecraftOverview onDetails={openDetails}/></div>
 <div className="row row3 home-row"><EnvironmentExplorer/><DataAnalytics/><HabitatSafetyAdvisor notify={notify} onDetails={openDetails}/></div><AIAgents onDetails={openDetails}/></>:<><div className="inner-header"><Header/></div><PageView page={page}/></>}
 </main>{page==='home'&&<BottomDashboards notify={notify} onDetails={openDetails}/>}
 {modal&&<div className="modal-back" onClick={()=>setModal(null)}><div className="modal panel" onClick={e=>e.stopPropagation()}><button className="modal-x" aria-label="Close" onClick={()=>setModal(null)}><X size={18}/></button><h3>{modal.title}</h3><div className="modal-body">{modal.body}</div></div></div>}{toast&&<div className="toast">{toast}</div>}</div>
}

import { render } from '@testing-library/react';
import './App.css';
import TrainerCard from './TrainerCard';
import TrainerCardIteration from './TrainerCardIteration';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">

//       </header>
//     </div>
//   );
// }

const App = () => {
  // return <TrainerCard/>;
  return (
    <div>
      
      <TrainerCardIteration/>
    </div>
  )
};

export default App;

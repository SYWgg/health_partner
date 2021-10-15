import React from 'react';
import TrainerCard from './TrainerCard';

// const style = {
//     list-style: "none",
// }

const TrainerCardIteration = () => {
    const trainerNames = ['김', '나', '박', '이'];
    const trainerList = trainerNames.map((name, index) => <div key={index}><TrainerCard/></div>);
    
    return <div>{trainerList}</div>;
};

export default TrainerCardIteration;
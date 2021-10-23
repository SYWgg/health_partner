import React from 'react';
import TrainerCard from './TrainerCard';
import { Grid } from '@mui/material';
// const style = {
//     list-style: "none",
// }

const TrainerCardIteration = () => {
    const trainerNames = ['김', '나', '박', '이', '김', '나', '박', '이', '김'];
    
    const trainerList = trainerNames.map((name, index) => <Grid item xs={4} key={index}><TrainerCard/></Grid>);
    

    return (
        <Grid container spacing={3}>{trainerList}</Grid>
        );
};

export default TrainerCardIteration;
import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';
// import trainerImage from './static/images/cards/User-Profile-PNG-Image.png'

export default function TrainerCard() {
  return (
    // default: 345
    <Card sx={{ maxWidth: 280 }}> 
      <CardActionArea>
        <CardMedia
          component="img"
          height="210"
          image={require('./static/images/cards/User-Profile-PNG-Image.png').default}
          alt="trainer image"
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            Lizard
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Lizards are a widespread group of squamate reptiles, with over 6,000
            species, ranging across all continents except Antarctica
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}
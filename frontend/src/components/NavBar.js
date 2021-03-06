import React from 'react';
import clsx from 'clsx';

import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Drawer from '@material-ui/core/Drawer';
import List from '@material-ui/core/List';
import Divider from '@material-ui/core/Divider';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import { NavLink } from 'react-router-dom';
import useScrollTrigger from '@material-ui/core/useScrollTrigger';
import Slide from '@material-ui/core/Slide';

export default function NavBar() {
  const trigger = useScrollTrigger();

  const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
    },
    menuButton: {
      marginRight: theme.spacing(2),
    },
    title: {
      flexGrow: 1,
    },
    offset: theme.mixins.toolbar,
  }));
  
  const [state, setState] = React.useState({
    left: false,
  });

  const classes = useStyles();

  const toggleDrawer = (anchor, open) => (event) => {
    if (event.type === 'keydown' && (event.key === 'Tab' || event.key === 'Shift')) {
      return;
    }

    setState({ ...state, [anchor]: open });
  };

  const url = '/'

  const list = (anchor) => (
    <div
      className={clsx(classes.list, {
        [classes.fullList]: anchor === 'top' || anchor === 'bottom',
      })}
      role="presentation"
      onClick={toggleDrawer(anchor, false)}
      onKeyDown={toggleDrawer(anchor, false)}
    >
      <List>
        <ListItem button component={NavLink} to="/" >
          <ListItemText primary={'Home'} />
        </ListItem>

        {['Animals', 'About'].map((text, index) => (
        <ListItem button component={NavLink} to={url + text.toLowerCase()} key={text}>
          {/* <ListItemIcon>{index % 2 === 0 ? <InboxIcon /> : <MailIcon />}</ListItemIcon> */}
          <ListItemText primary={text} />
        </ListItem>
        ))}

        <Divider />
      
        <ListItem button component={NavLink} to='/zoos'>
          <ListItemText primary='For Zookeepers' />
        </ListItem>
      </List>
      
    </div>
  );

  return (
    <div className={classes.root}>
      <Slide appear={false} in={!trigger}>
      <AppBar position="fixed">
        <Toolbar>
        
        {['left'].map((anchor) => (
          <React.Fragment key={anchor}>
          <IconButton edge="start" className={classes.menuButton} onClick={toggleDrawer(anchor, true)} color="inherit" aria-label="menu">
            <MenuIcon />
          </IconButton>
          <Drawer anchor={anchor} open={state[anchor]} onClose={toggleDrawer(anchor, false)}>
            {list(anchor)}
          </Drawer>
          </React.Fragment>
        ))}
        
          <Typography variant="h5" component='h1' className={classes.title}>
            WildWish
          </Typography>
          {/* <Button color="inherit">Login</Button> */}
        </Toolbar>
      </AppBar>
      </Slide>
      <div className={classes.offset} />
    </div>
    
  );
}
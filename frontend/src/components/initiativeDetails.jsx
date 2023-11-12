import * as React from "react";
import { styled, createTheme, ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import MuiDrawer from "@mui/material/Drawer";
import Box from "@mui/material/Box";
import MuiAppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import List from "@mui/material/List";
import Typography from "@mui/material/Typography";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Paper from "@mui/material/Paper";
import Link from "@mui/material/Link";
import MenuIcon from "@mui/icons-material/Menu";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import { mainListItems, secondaryListItems } from "./listItems";
import Initiatives from "./Initiatives";
import Title from "./Title";
import { Stack } from "@mui/material";
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material';

function Copyright(props) {
  return (
    <Typography
      variant="body2"
      color="text.secondary"
      align="center"
      {...props}
    >
      {"Copyright © "}
      <Link color="inherit" href="/">
        ImpactPulse
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

const drawerWidth = 240;

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(["width", "margin"], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(["width", "margin"], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

const Drawer = styled(MuiDrawer, {
  shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
  "& .MuiDrawer-paper": {
    position: "relative",
    whiteSpace: "nowrap",
    width: drawerWidth,
    transition: theme.transitions.create("width", {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
    boxSizing: "border-box",
    ...(!open && {
      overflowX: "hidden",
      transition: theme.transitions.create("width", {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
      }),
      width: theme.spacing(7),
      [theme.breakpoints.up("sm")]: {
        width: theme.spacing(9),
      },
    }),
  },
}));

// TODO remove, this demo shouldn't need to reset the theme.
const theme = createTheme({
  palette: {
    primary: {
      main: "#7E52A0",
    },
    secondary: {
      main: "#58A4B0",
    },
  },
});

export default function InitiativeDetails() {
  const [open, setOpen] = React.useState(false);
  const toggleDrawer = () => {
    setOpen(!open);
  };

  return (
    <ThemeProvider theme={theme}>
      <Box sx={{ display: "flex" }}>
        <CssBaseline />
        <AppBar position="absolute" open={open}>
          <Toolbar
            sx={{
              pr: "24px", // keep right padding when drawer closed
            }}
          >
            <IconButton
              edge="start"
              color="inherit"
              aria-label="open drawer"
              onClick={toggleDrawer}
              sx={{
                marginRight: "36px",
                ...(open && { display: "none" }),
              }}
            >
              <MenuIcon />
            </IconButton>
            <Typography
              component="h1"
              variant="h6"
              color="inherit"
              noWrap
              sx={{ flexGrow: 1 }}
            >
              Dashboard
            </Typography>
            ImpactPulse
          </Toolbar>
        </AppBar>
        <Drawer variant="permanent" open={open}>
          <Toolbar
            sx={{
              display: "flex",
              alignItems: "center",
              justifyContent: "flex-end",
              px: [1],
            }}
          >
            <IconButton onClick={toggleDrawer}>
              <ChevronLeftIcon />
            </IconButton>
          </Toolbar>
          <Divider />
          <List component="nav">
            {mainListItems}
            <Divider sx={{ my: 1 }} />
            {secondaryListItems}
          </List>
        </Drawer>
        <Box
          component="main"
          sx={{
            backgroundColor: (theme) =>
              theme.palette.mode === "light"
                ? theme.palette.grey[100]
                : theme.palette.grey[900],
            flexGrow: 1,
            height: "100vh",
            overflow: "auto",
          }}
        >
          <Toolbar />
          <Container maxWidth="md" sx={{ mt: 4, mb: 4 }}>
            <Title>Hackathon</Title>

            <Grid item xs={12}>
              <Paper sx={{ p: 2, display: "flex", flexDirection: "column" }}>
                <Grid item xs={12} md={4} lg={3}>
                  <Paper
                    sx={{
                      p: 2,
                      display: "flex",
                      flexDirection: "column",
                      height: 150,
                      width: 200,
                    //   color: (theme) => theme.palette.primary.main,
                      marginBottom: 2,
                      backgroundColor: (theme) => theme.palette.secondary.main,
                    }}
                  >
                    <Stack
                      direction="column"
                      justifyContent="flex-start"
                      alignItems="center"
                      spacing={2}
                    >
                      <Typography variant="h2" component="div" color='white'>
                        6.7
                      </Typography>
                      <Typography variant="h7" component="div" color='white'>
                        Average Score
                      </Typography>
                    </Stack>
                  </Paper>

                    <TableContainer component={Paper}style={{ width: '100%' }}>
                       
                      <Table>
                        <TableHead>
                          <TableRow>
                            <TableCell>Details</TableCell>
                            <TableCell>Count</TableCell>
                            <TableCell align="center">Heart Rate</TableCell>
                          </TableRow>
                        </TableHead>
                        <TableBody>
                          <TableRow>
                            <TableCell>Applicants</TableCell>
                            <TableCell>1000</TableCell>
                            <TableCell align="center">1.2</TableCell>
                          </TableRow>
                          <TableRow>
                            <TableCell>Participants</TableCell>
                            <TableCell>125</TableCell>
                            <TableCell align="center">2.1</TableCell>
                          </TableRow>
                          <TableRow>
                            <TableCell>Teams</TableCell>
                            <TableCell>10</TableCell>
                            <TableCell align="center">1.0</TableCell>
                          </TableRow>
                          <TableRow>
                            <TableCell>Judges</TableCell>
                            <TableCell>5</TableCell>
                            <TableCell align="center">.08</TableCell>
                          </TableRow>
                          <TableRow>
                            <TableCell>Mentors</TableCell>
                            <TableCell>12</TableCell>
                            <TableCell align="center">.08</TableCell>
                          </TableRow>
                          <TableRow>
                            <TableCell>Nationalities</TableCell>
                            <TableCell>45</TableCell>
                            <TableCell align="center">.08</TableCell>
                          </TableRow>
                        </TableBody>
                      </Table>
                    </TableContainer>

                </Grid>
              </Paper>
            </Grid>

            <Copyright sx={{ pt: 4 }} />
          </Container>
        </Box>
      </Box>
    </ThemeProvider>
  );
}

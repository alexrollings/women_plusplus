import * as React from "react";
import Box from "@mui/material/Box";
import List from "@mui/material/List";
import Grid from "@mui/material/Grid";
import Link from "@mui/material/Link";
import Paper from "@mui/material/Paper";
import Title from "./Title";
import Table from "@mui/material/Table";
import Toolbar from "@mui/material/Toolbar";
import Divider from "@mui/material/Divider";
import MenuIcon from "@mui/icons-material/Menu";
import TableRow from "@mui/material/TableRow";
import Container from "@mui/material/Container";
import MuiDrawer from "@mui/material/Drawer";
import MuiAppBar from "@mui/material/AppBar";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableHead from "@mui/material/TableHead";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import CssBaseline from "@mui/material/CssBaseline";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import { mainListItems, secondaryListItems } from "./listItems";
import { styled, createTheme, ThemeProvider } from "@mui/material/styles";


//reusing nav code on every page - need to confuigure app to be wrapped with nav
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
function createData(id, date, name, description, score) {
  return { id, date, name, description, score };
}

//data for table - need to make dynamic/connected to db
const rows = [
  createData(
    5,
    "10 Oct, 2023",
    "Hackathon",
    "A competive event where teams of programmers and designers collaborate...",
    8.1
  ),
  createData(
    2,
    "10 Dec, 2022",
    "Javascript Class",
    "A class to teach the basics of Javascript.",
    7.1
  ),
  createData(
    4,
    "10 Sep, 2023",
    "Beginner Python Class",
    "A class to teach the basics of Python.",
    6.7
  ),
  createData(
    0,
    "16 Mar, 2022",
    "Hackathon",
    "A competive event where teams of programmers and designers collaborate...",
    5.5
  ),
  createData(
    3,
    "11 Mar, 2023",
    "Hackathon",
    "A competive event where teams of programmers and designers collaborate...",
    5.2
  ),
  createData(
    1,
    "4 Aug, 2022",
    "Demo Days",
    "A showcase of the projects that were created.",
    3.2
  ),
];

export default function GoalDetails() {
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
              Goal Details
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
          <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
            <Title>Include Women In Tech</Title>
            <Grid item xs={12}>
              <Paper sx={{ p: 2, display: "flex", flexDirection: "column" }}>
                <Table size="medium">
                  <TableHead>
                    <Title>Initiatives by Rank</Title>
                    <TableRow>
                      <TableCell>Date</TableCell>
                      <TableCell>Name</TableCell>
                      <TableCell>Description</TableCell>
                      <TableCell>Heartbeat</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {rows.map((row) => (
                      <TableRow key={row.id} hover="true">
                        <TableCell>{row.date}</TableCell>
                        <TableCell>
                          <Link
                            underline="none"
                            color={"black"}
                            href={`/initiatives/${row.id}`}
                          >
                            {row.name}
                          </Link>
                        </TableCell>
                        <TableCell>{row.description}</TableCell>
                        <TableCell>{row.score}</TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </Paper>
            </Grid>
          </Container>
        </Box>
      </Box>
    </ThemeProvider>
  );
}

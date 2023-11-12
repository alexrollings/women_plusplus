import * as React from "react";
import LogoutIcon from '@mui/icons-material/Logout';
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import ListSubheader from "@mui/material/ListSubheader";
import DashboardIcon from "@mui/icons-material/Dashboard";
import AssessmentIcon from "@mui/icons-material/Assessment";
import ListItemButton from "@mui/material/ListItemButton";
import CollectionsIcon from "@mui/icons-material/Collections";
import SportsScoreIcon from "@mui/icons-material/SportsScore";
import BusinessCenterIcon from "@mui/icons-material/BusinessCenter";

import { Link } from "@mui/material";

export const mainListItems = (
  <React.Fragment>
    <Link href="/dashboard" underline="none" color="black">
      <ListItemButton>
        <ListItemIcon>
          <DashboardIcon />
        </ListItemIcon>
        <ListItemText primary="Dashboard" />
      </ListItemButton>
    </Link>
    <Link href="/goals" underline="none" color="black">
    <ListItemButton>
      <ListItemIcon>
        <SportsScoreIcon />
      </ListItemIcon>
      <ListItemText primary="Goals" />
    </ListItemButton>
    </Link>
    <Link href="/initiatives" underline="none" color="black">
      <ListItemButton>
        <ListItemIcon>
          <BusinessCenterIcon />
        </ListItemIcon>
        <ListItemText primary="Initiatives" />
      </ListItemButton>
    </Link>
    <ListItemButton>
      <ListItemIcon>
        <CollectionsIcon />
      </ListItemIcon>
      <ListItemText primary="Collect" />
    </ListItemButton>
    <ListItemButton>
      <ListItemIcon>
        <AssessmentIcon />
      </ListItemIcon>
      <ListItemText primary="Reports" />
    </ListItemButton>
  </React.Fragment>
);

export const secondaryListItems = (
  <React.Fragment>
    <ListSubheader component="div" inset></ListSubheader>
    <Link href="/" underline="none" color="black">
    <ListItemButton>
      <ListItemIcon>
        <LogoutIcon />
      </ListItemIcon>
      <ListItemText primary="Logout" />
    </ListItemButton>
    </Link>
  </React.Fragment>
);

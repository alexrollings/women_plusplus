import * as React from 'react';
import Link from '@mui/material/Link';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import AddIcon from "@mui/icons-material/Add";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Modal from "@mui/material/Modal";
import Typography from "@mui/material/Typography";
import Stack from "@mui/material/Stack";
import { useState } from "react";
import TextField from "@mui/material/TextField";
import Title from "./Title";
import Fade from '@mui/material/Fade';
import Tooltip from '@mui/material/Tooltip';

// Generate Order Data
function createData(id, date, name, description, score) {
  return { id, date, name, description, score };
}

const rows = [
  createData(
    5,
    "10 Oct, 2023",
    "Hackathon",
    "A competive event where teams of programmers and designers collaborate...",
    8.1
  ),
  createData(
    4,
    "10 Sep, 2023",
    "Beginner Python Class",
    "A class to teach the basics of Python.",
    6.7
  ),
  createData(
    3,
    "11 Mar, 2023",
    "Hackathon",
    "A competive event where teams of programmers and designers collaborate...",
    5.2
  ),
  createData(
    2,
    "10 Dec, 2022",
    "Javascript Class",
    "A class to teach the basics of Javascript.",
    7.1
  ),
  createData(
    1,
    "4 Aug, 2022",
    "Demo Days",
    "A showcase of the projects that were created.",
    3.2
  ),
  createData(
    0,
    "16 Mar, 2022",
    "Hackathon",
    "A competive event where teams of programmers and designers collaborate...",
    5.5
  ),
];
      function preventDefault(event) {
        event.preventDefault();
      };

const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 400,
  bgcolor: "background.paper",
  border: "2px solid #000",
  boxShadow: 24,
  borderRadius: '5px',
  p: 4,
};



export default function Initiatives() {
  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const [name, setName] = useState("");
  const [itemDescription, setItemDescription] = useState("")
  const [eventURL, setEventURL] = useState("")

  const handleAddInit = () => {
    rows.push(createData(
      rows.length,
      new Date().toLocaleDateString(),
      name,
      itemDescription
    ))
    handleClose()
  }

  return (
    <React.Fragment>
      <Stack direction="row" justifyContent="space-between">
        <Title>Recent Initiatives</Title>
        <Tooltip
          TransitionComponent={Fade}
          TransitionProps={{ timeout: 600 }}
          title="Add"
        >

        <Button onClick={handleOpen} sx={{
          color: 'white',
          backgroundColor: (theme) => theme.palette.primary.main
          }}>
          Add a new initiative<AddIcon fontSize="medium" />
        </Button>
        </Tooltip>
      </Stack>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            Add a new Initiative
          </Typography>
          <Typography id="modal-modal-description" sx={{ mt: 2 }}>
            <Stack spacing={4}>
              <TextField
                id="standard-basic"
                label="Name of Initiative"
                variant="standard"
                value={name}
                onChange={(event) => {
                  setName(event.target.value);
                }}
              />
              <TextField
                id="outlined-multiline-static"
                label="Details"
                multiline
                rows={4}
                defaultValue="Please add your initiative details here."
                value={itemDescription}
                onChange={(event) => {
                  setItemDescription(event.target.value);
                }}
                />
                <TextField
                id="standard-basic"
                label="Event URL"
                variant="standard"
                value={eventURL}
                onChange={(event) => {
                  setName(event.target.value);
                }}
              />
              <Button variant="contained" onClick={handleAddInit}>
                Add
              </Button>
            </Stack>
          </Typography>
        </Box>
      </Modal>

      <Table size="medium">
        <TableHead>
          <TableRow>
            <TableCell>Date</TableCell>
            <TableCell>Name</TableCell>
            <TableCell>Description</TableCell>
            <TableCell>Heart Rate</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id} hover="true">
              <TableCell>{row.date}</TableCell>
              <TableCell>
                <Link underline="none" color={"black"} href={`/initiatives/${row.id}`}>
                  {row.name}
                </Link>
              </TableCell>
              <TableCell>{row.description}</TableCell>
              <TableCell>{row.score}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </React.Fragment>
  );
}

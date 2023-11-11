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

// Generate Order Data
function createData(id, date, name, description) {
  return { id, date, name, description};
}

const rows = [
  createData(
    0,
    "16 Mar, 2019",
    "Elvis Presley",
    "description"
  ),
  createData(
    1,
    "16 Mar, 2019",
    "Paul McCartney",
    "description"
  ),
  createData(
    2,
    "16 Mar, 2019",
    "Tom Scholz",
    "description"
  ),
  createData(
    3,
    "16 Mar, 2019",
    "Michael Jackson",
    "description"
  ),
  createData(
    4,
    "15 Mar, 2019",
    "Bruce Springsteen",
    "description"
  ),
];

function preventDefault(event) {
  event.preventDefault();
}

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
        <Button onClick={handleOpen}>
          <AddIcon fontSize="large" />
        </Button>
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
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id} hover="true">
              <TableCell>{row.date}</TableCell>
              <TableCell>
                <Link underline='none' color={'black'} href={`/${row.id}`}>{row.name}</Link>
              </TableCell>
              <TableCell>{row.description}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </React.Fragment>
  );
}

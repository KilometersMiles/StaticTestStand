# Static Test Stand
A test stand to measure a force-time curve for small rocket motors. This is designed for collecting data on small A-class motors. 

## Onshpae Link
The files are available for download here on the github or you can use the onshape document.
https://cad.onshape.com/documents/dc1ea5a17a6875eff156904f/w/99ff55d2b2f774a85729f015/e/69d40390ca9ec5910e336e51?renderMode=0&uiState=6a68344a8ce625604a90d9ac

## Build Instructions
1. Obtain all materials
  - 3D Print Adapter Square and motor mount.
  - 3 10 Hole GoBilda U-Channel and 2 GoBilda quad blocks.
  - 16 M4 Screws and Bolts
  - Raspberry PI Pico
  - HX711 and 5kg Load Cell
  - USB Micro Battery Pack
2. Wiring
Follow this diagram. Made in Cirkit Designer. Link: https://app.cirkitdesigner.com/project/235e4502-1041-476a-81f1-36d9f1a2d234
<img width="1037" height="779" alt="image" src="https://github.com/user-attachments/assets/fd2c64ff-410d-4fd8-9186-4562af728626" />
3. Build
  - Use 2 M4 screws to mount the quad blocks to the end of two U-Channels
   <img width="1584" height="1148" alt="image" src="https://github.com/user-attachments/assets/3771f7e2-80b1-466a-8660-eeba5c75730f" />
  - Attach these to the third U-Channel using two more M4 Screws on each side.
   <img width="1599" height="922" alt="image" src="https://github.com/user-attachments/assets/cba2d104-073d-44cb-b086-c137ce083b1c" />
  - Screw in the Adapter Square to the third U-channel using the 4 corner holes and 4 M4 Screws. Make sure the center of the square is over a hole
    <img width="1001" height="702" alt="image" src="https://github.com/user-attachments/assets/a7d859a9-a044-423c-af54-c5846d3a75b7" />
  - Screw in the Load Cell to the Adapter Square
   <img width="1005" height="708" alt="image" src="https://github.com/user-attachments/assets/b59e72fa-a81b-4666-80e4-89f1438e054d" />
  - Screw in the Motor Mount to the Load Cell
    <img width="1017" height="720" alt="image" src="https://github.com/user-attachments/assets/1049cc30-246e-485f-8817-2cc30aef28e6" />

## Test Instructions
Download the code from the code folder and upload it using Thonny.
To start recording data for 30 seconds, plug in the battery. The recording starts automatically. 
Use Thonny to then view/export the generated CSV file holding the data.


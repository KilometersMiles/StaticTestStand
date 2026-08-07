# Static Test Stand
A test stand to measure a force-time curve for small rocket motors. This is designed for collecting data on small A-class motors. 

## Onshape Link
The files are available for download here on the Github or you can use the Onshape document.
https://cad.onshape.com/documents/dc1ea5a17a6875eff156904f/w/99ff55d2b2f774a85729f015/e/69d40390ca9ec5910e336e51?renderMode=0&uiState=6a68344a8ce625604a90d9ac

## Bill of Materials

| Name | Quantity | Price Per Unit | Total Price | Link |  | Grand Total: | 80.57 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Load Cell/HX711 Module | 1 | 6.79 | 6.79 | https://www.amazon.com/NOYITO-10kg-20kg-HX711-Combo/dp/B07BGXXHSW/ref=sr_1_5?crid=197VVABTEKJQQ&amp;dib=eyJ2IjoiMSJ9.kHxQpWmDJPGyCP5Uup8r37mMZczCyrsi69sl7BJy74X5sW9IzJWoBeYHE9zrZEqMYmBbfHH2-hrchu9hbTXlx0qH5CigyC-EWpMwT9n-Wfrz174pxAPxtiX36HHxVDkPOxYoBUExEhKGvwMbG9l1yt9VTicDE0J26EGeoq74yIpOA1CU7RwhSRaneNYmIEdcEb-WVp6VuQHTf39e0dtOqy-7HsNqhm8HcOpWGJFGjlY.fMe7MhnEYP1zP5x3tSKBZzWUPkeTzOCAzQSnDbJGm8o&amp;dib_tag=se&amp;keywords=hx711%2Bload%2Bcell%2B5kg&amp;qid=1785442292&amp;sprefix=hx711%2Bload%2Bcell%2B5kg%2Caps%2C183&amp;sr=8-5&amp;th=1 |  |  |  |
| goBilda U Channel 10 Hole | 3 | 13.99 | 41.97 | https://www.gobilda.com/1120-series-u-channel-10-hole-264mm-length/ |  |  |  |
| goBilda Quad Block | 2 | 6.99 | 13.98 | https://www.gobilda.com/1201-series-quad-block-pattern-mount-43-2/ |  |  |  |
| Raspberry PI Pico | 1 | 7.84 | 7.84 | https://www.amazon.com/Raspberry-Pi-Pico/dp/B09KVB8LVR/ref=sr_1_1_mod_primary_new?dib=eyJ2IjoiMSJ9.KhN-eo1QUief6dgXnlRewOD_5s_2kVFK-6pw5wXpUoenhfEziNw1EZu28KJJY-NPeuf40LrYKOKfojRINgbYCNdlD9l1FMnYgn17isNOgJG86847zgtTK8lLedytnSqAUOMMG5zn19O2kiVBvb7pn0V19VgkroKPfF1D3lVifm6wSIpVeY_ky9USfTRkxL6h-WL_YPp1xyiZtFcToBs2wKD70macTw9-K_JlD5AbiMU.g0UX7KZKLAg6Tf6kyleGFS-Qh_fRqNLIm8AmfQSzFm0&amp;dib_tag=se&amp;hvadid=693924362546&amp;hvdev=c&amp;hvexpln=67&amp;hvlocphy=9029754&amp;hvnetw=g&amp;hvocijid=7542336006660959476--&amp;hvqmt=e&amp;hvrand=7542336006660959476&amp;hvtargid=kwd-1966451685986&amp;hydadcr=24333_13517641&amp;keywords=raspberry-pi+pico&amp;mcid=7acc28fd414f302ea899a696a011ae6b&amp;qid=1785442529&amp;sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&amp;sr=8-1 |  |  |  |
| Breadboard &amp; Jumper Wires Kit | 1 | 9.99 | 9.99 | https://www.amazon.com/BOJACK-Values-Solderless-Breadboard-Flexible/dp/B08Y59P6D1/ref=sr_1_1_sspa?crid=1SWCH971KDWVQ&amp;dib=eyJ2IjoiMSJ9.KciiFgkRrEIcipCiSmynt7Crly9TE4zJeJX-FA7JYDExtGNpdGHdyXMK3MGmjSwQqXhjN3WbOo8SWoeOZSYGljXTztNQMgZFbQcje4naGDwktjg9PmafUU4aTea0FEhwgqeU81dzRBiA2NVw2yzdTaC3zm2z0QNRfoRQtxzgXoXkvz-CbPC3lhwfFMZtkzbSJYmy_Gl1PbC8cwWrwqNA_j3EuNwZeNtmIKXh7eQ2kag.ShPTAHOruLjIN4_MHw4KjmXVJrGK5_QqOUcMMB3-5j0&amp;dib_tag=se&amp;keywords=breadboard%2Bone%2Bpiece&amp;qid=1785442628&amp;sprefix=breadboard%2Bone%2Bpiec%2Caps%2C169&amp;sr=8-1-spons&amp;sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&amp;th=1 |  |  |  |
| Motor Mount | 1 | Printed |  |  |  |  |  |
| Blast Shield | 1 | Printed |  |  |  |  |  |
| goBilda to Load Cell Adapter | 1 | Printed |  |  |  |  |  |

## Build Instructions
1. Obtain all materials
  - 3D Print Adapter Square, Blast Shield and Motor Mount.
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
  - Place electronic system in corner of U-Channel
   <img width="591" height="341" alt="image" src="https://github.com/user-attachments/assets/2e4d2adb-516b-4ece-a6ae-5155c5a026ba" />
   - Secure the sheild with 4 M4 Screws
     <img width="940" height="556" alt="image" src="https://github.com/user-attachments/assets/051bcb20-fe29-4b4c-a3c9-d18d1d3e58a0" />

## Test Instructions
Download the code from the code folder and upload it using Thonny.
To start recording data for 30 seconds, plug in the battery. The recording starts automatically. 
Use Thonny to then view/export the generated CSV file holding the data.


# V0.2

## Goal
Allow for clipboard data (text, files, images) to be securely transferred between devices. The application will serve as both a client and server for 1-to-1 clipboard sharing.

---

## Plan
### Features
- Clipboard transfer of text, files, and potentially images.
- Secure and reliable data transfer over the network.
- User-friendly commands for initiating, accepting, or rejecting transfers.
- Error handling for edge cases like invalid inputs or interrupted connections.

---

## Flow
1. **Application Start**
   - User types `ss` to initialize the app.
     - Initializes necessary classes:
       - **Sending Data**: Handles outgoing clipboard data.
       - **Receiving Data**: Handles incoming requests and data.
       - **Analyzing Data**: Processes clipboard contents.
       - **Sanitizing Input**: Validates and secures user input and data.

2. **Sending Clipboard Data**
   - User enters the recipient's hostname or IP address.
   - System performs the following:
     1. Validate the address.
     2. Access clipboard data using `getFromClipboard()`.
     3. Analyze clipboard data:
        - `getFileType()`
        - `getFileSize()`
        - `getFileEncoding()`
     4. Sanitize and prepare the data for sending.
     5. Request transfer approval from the recipient.
     6. If approved:
        - Establish connection.
        - Transmit the clipboard data.
        - Provide progress updates.

3. **Receiving Clipboard Data**
   - Recipient receives a transfer request.
   - System prompts the recipient to accept or deny with a `y/n` input.
   - If accepted:
     - Validates incoming data for size, type, and compatibility.
     - Stores the data in the recipient's clipboard or a specified location.

4. **Transfer Completion**
   - Sender and recipient receive success or failure feedback.
   - Logs the transfer details for debugging and user reference.

---

## Commands
- **`ss`**: Start the application.
- **`ss send <hostname/IP>`**: Send clipboard data to a specific recipient.
- **`ss history`**: View logs of recent transfers.
- **`ss quit`**: Terminate the application.
- **Ctrl+C**: Interrupt and terminate send/receive threads.

---

## Error Handling
1. **Invalid Address**: Prompt the user to re-enter a valid hostname or IP.
2. **Empty Clipboard**: Notify the user and halt the transfer.
3. **Timeouts**: Automatically terminate requests after a set period of inactivity.
4. **Network Errors**: Retry transfer or notify the user of a failure.
5. **Unsupported Formats**: Alert the user and skip incompatible clipboard contents.

---

## Security
1. **Encryption**: Use AES or TLS to secure data during transfer.
2. **Authentication**: Pair devices using a shared key, QR code, or password.
3. **Rate Limiting**: Prevent spam by limiting the number of transfer requests per minute.
4. **Input Sanitization**: Ensure addresses and clipboard contents are safe and valid.

---

## Future Enhancements
1. **Multi-Device Support**: Allow 1-to-N clipboard sharing.
2. **Cross-Network Functionality**: Implement NAT traversal or a relay server for devices on different networks.
3. **Enhanced Clipboard Support**: Add support for rich text, images, and other complex formats.
4. **Transfer Queueing**: Handle multiple incoming/outgoing requests efficiently.
5. **Compression**: Compress large files for faster transfers.

---

## Technical Notes
- **Concurrency**: Ensure thread safety when accessing the clipboard and handling network I/O.
- **Cross-Platform Compatibility**: Test and implement for Windows, macOS, and Linux.
- **Logs**: Maintain detailed logs for debugging and future development.

---

## Example Workflow
1. User types `ss`.
2. User copies text to the clipboard.
3. User types `ss send <hostname/IP>`.
4. The recipient receives a request and types `y` to accept.
5. Data is securely transferred and placed in the recipient's clipboard.
6. Both sender and recipient are notified of the success.
7. Transfer threads are terminated with Ctrl+C if needed.

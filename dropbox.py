import dropbox

client = dropbox.client.DropboxClient(
    sl.AuEQb5QQOZ1D7TBUEjry158TNncVoJafaGN13WkSuKoH43pIK_sjSvV2FSaHbjSl
    - q4KaA2k7KMHKgVMdPySQ14SKCqCjFa4JjTfEt61yXM84awjgoczrIH9U0aCoxQ5Fi
    - TjAQ
)
print("linked account: ", client.account_info())

f = open("base_datos.db", "rb")
response = client.put_file("/magnum-opus.txt", f)
print("uploaded: ", response)

folder_metadata = client.metadata("/")
print("metadata: ", folder_metadata)

f, metadata = client.get_file_and_metadata("/magnum-opus.txt")
out = open("magnum-opus.txt", "wb")
out.write(f.read())
out.close()
print(metadata)

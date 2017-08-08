class Outputer(object):
    _collection=[]
    def collecting(self, data):
        if data is None:
            return
        self._collection.append(data)

    def outputing(self):
        fout=open('result.html','w')
        fout.write('<html>')
        fout.write('<head><meta charset="utf-8"></head>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self._collection:
            fout.write('<tr>')
            fout.write(r'<td>%s</td>' % data['text'].encode('utf-8'))
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()